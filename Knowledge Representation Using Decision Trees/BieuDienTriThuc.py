import numpy as np
# Dùng phương pháp information gain
class Node:
    def __init__(self, feature_idx=None, threshold=None, left=None, right=None, value=None):
        self.feature_idx = feature_idx
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTree:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def entropy(self, y):
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))
        return entropy

    def information_gain(self, X, y, feature_idx, threshold):
        left_mask = X[:, feature_idx] <= threshold
        right_mask = ~left_mask
        left_entropy = self.entropy(y[left_mask])
        right_entropy = self.entropy(y[right_mask])
        parent_entropy = self.entropy(y)
        information_gain = parent_entropy - (len(y[left_mask]) / len(y) * left_entropy) - (len(y[right_mask]) / len(y) * right_entropy)
        return information_gain

    def find_best_split(self, X, y):
        best_gain = 0
        best_feature_idx = None
        best_threshold = None
        n_features = X.shape[1]

        for feature_idx in range(n_features):
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                gain = self.information_gain(X, y, feature_idx, threshold)
                if gain > best_gain:
                    best_gain = gain
                    best_feature_idx = feature_idx
                    best_threshold = threshold

        return best_feature_idx, best_threshold

    def build_tree(self, X, y, depth):
        if depth == self.max_depth or len(y) < self.min_samples_split or len(np.unique(y)) == 1:
            value = np.bincount(y).argmax()
            return Node(value=value)

        feature_idx, threshold = self.find_best_split(X, y)
        if feature_idx is None or threshold is None:
            value = np.bincount(y).argmax()
            return Node(value=value)

        left_mask = X[:, feature_idx] <= threshold
        right_mask = ~left_mask
        left_node = self.build_tree(X[left_mask], y[left_mask], depth + 1)
        right_node = self.build_tree(X[right_mask], y[right_mask], depth + 1)

        return Node(feature_idx=feature_idx, threshold=threshold, left=left_node, right=right_node)

    def fit(self, X, y):
        self.tree = self.build_tree(X, y, depth=0)

    def predict_single(self, x, node):
        if node.value is not None:
            return node.value

        if x[node.feature_idx] <= node.threshold:
            return self.predict_single(x, node.left)
        else:
            return self.predict_single(x, node.right)

    def predict(self, X):
        y_pred = []
        for x in X:
            y_pred.append(self.predict_single(x, self.tree))
        return np.array(y_pred)

def read_data_from_file(file_path):
    with open(file_path, 'r', encoding="UTF-8") as file:
        lines = file.readlines()

    attributes = lines[0].strip().split(', ')
    data = []
    labels = []

    for line in lines[1:]:
        values = line.strip().split(', ')
        data.append(values[:-1])
        labels.append(values[-1])

    return np.array(data), np.array(labels), attributes

X,y,att = read_data_from_file("DataTrainDT.txt")

att[0] = att[0].replace('\ufeff', '')
print("Các thông tin của thuộc tính", att)

# Chuyển đổi các thuộc tính chuỗi thành số nguyên
attribute_mapping = {}
X_encoded = np.empty(X.shape)
for i in range(X.shape[1]):
    attribute_values = np.unique(X[:, i])
    attribute_mapping[i] = {value: idx for idx, value in enumerate(attribute_values)}
    X_encoded[:, i] = np.array([attribute_mapping[i][value] for value in X[:, i]])

# Chuyển đổi nhãn chuỗi thành số nguyên
label_values = np.unique(y)
label_mapping = {value: idx for idx, value in enumerate(label_values)}
y_encoded = np.array([label_mapping[label] for label in y])

# Xây dựng mô hình cây quyết định
dt = DecisionTree(max_depth=3)
dt.fit(X_encoded, y_encoded)

# Chuỗi thuộc tính của câu cần dự đoán
sentence = np.array(['nắng', 'xấu', 'không tham gia', 'lạnh'])

# Chuyển đổi các giá trị thuộc tính chuỗi thành số nguyên
sentence_encoded = np.empty(sentence.shape)
for i in range(sentence.shape[0]):
    sentence_encoded[i] = attribute_mapping[i][sentence[i]]

# Dự đoán nhãn cho câu
predicted_label = dt.predict_single(sentence_encoded, dt.tree)

# Chuyển đổi nhãn số nguyên thành nhãn chuỗi
predicted_label_decoded = label_values[predicted_label]

# In kết quả dự đoán
print("Dự đoán cho câu '{}' là '{}'.".format(' '.join(sentence), predicted_label_decoded))
