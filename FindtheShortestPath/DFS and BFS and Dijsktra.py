# from collections import defaultdict
# from typing import Dict, Tuple
#
#
# def katz_backoff_2gram_prob(text, lambda_1, lambda_2, lambda_3):
#     # Tính toán số lần xuất hiện của các từ đơn
#     word_counts = defaultdict(int)
#     for word in text.split():
#         word_counts[word] += 1
#
#     # Tính toán số lần xuất hiện của các 2-gram
#     bigram_counts = defaultdict(int)
#     words = text.split()
#     for i in range(len(words) - 1):
#         bigram_counts[(words[i], words[i + 1])] += 1
#
#     # Tính toán xác suất cơ bản của các 2-gram
#     basic_probs = {}
#     for bigram, count in bigram_counts.items():
#         word1 = bigram[0]
#         basic_probs[bigram] = count / word_counts[word1]
#
#     # Tính toán xác suất của các 2-gram theo mô hình back-off
#     backoff_probs = {}
#     for bigram, count in bigram_counts.items():
#         word1 = bigram[0]
#         word2 = bigram[1]
#         if count > 0 :
#             # Sử dụng xác suất cơ bản nếu 2-gram xuất hiện trong tập huấn luyện
#             backoff_probs[bigram] = lambda_1 * basic_probs[bigram] + lambda_2 * basic_probs[(word2,)] + lambda_3
#
#         else:
#             # Tìm các 2-gram gần giống với (w1, w2)
#             # Tìm các 2-gram có từ đầu tiên là w1
#             candidate_bigrams = [(w1, w) for (w1, w) in bigram_counts.keys() if w1 == word1]
#             # Nếu không tìm thấy 2-gram nào, tìm các 2-gram có từ thứ hai là w2
#             if len(candidate_bigrams) == 0:
#                 candidate_bigrams = [(w, w2) for (w, w2) in bigram_counts.keys() if w2 == word2]
#             # Tính tỷ lệ đếm của các 2-gram gần giống so với tổng số 2-gram xuất hiện trong tập huấn luyện
#             candidate_counts = sum([bigram_counts[cb] for cb in candidate_bigrams])
#             if candidate_counts > 0:
#                 # Sử dụng mô hình back-off để tính toán xác suất
#                 backoff_probs[bigram] = lambda_2 * basic_probs[(word2,)] + lambda_3
#             else:
#                 # Nếu không tìm thấy 2-gram nào gần giống, sử dụng xác suất back-off cuối cùng
#                 backoff_probs[bigram] = lambda_3
#
#     return backoff_probs
#
# text = "I like to eat pizza. Pizza is my favorite food. I eat pizza every day."
#
# lambda_1=0.7
# lambda_2=0.2
# lambda_3=0.1
# # Tính toán xác suất của các 2-gram trong đoạn văn bản
# probs = katz_backoff_2gram_prob(text, lambda_1, lambda_2, lambda_3)
#
# # In kết quả ra màn hình
# for bigram, prob in probs.items():
#     print(f"{bigram[0]} {bigram[1]}: {prob:.4f}")
#
#


x= ((2/3)*(1/3))/(1/6)
y= ((1/3)*(2/3))/(1/6)
print(x+y)