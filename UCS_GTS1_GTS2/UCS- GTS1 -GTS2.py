
import numpy as np
import pandas as pd

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, v1, v2, cost):
        # cho đồ thị có hướng
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].append([v2, cost])

    """Giải thuật UCS"""
    def UCS(self, start, end):
        visited = set()
        priority_queue = [(0, start, [])]  # Hàng đợi ưu tiên chứa (cost, điểm đang xét, và đường đi)
        while priority_queue:
            (cost, node, path) = priority_queue.pop(0)
            if node not in visited: # đánh dấu viến thăm
                visited.add(node)
            if node == end: # nếu đụng điểm cuối thì đưa vào các đường đi
                return path+[node], cost # luus lại thông tin
            """ Duyệt qua các đỉnh và các điểm"""
            for neighbor, neighbor_cost in self.vertices[node]:
                # Nếu chưa viến thăm thì tiếp tục và đã viến thăm thì sắp xếp lại
                if neighbor not in visited:
                    """Thêm dữ liệu đường đi mới vào priority
                    _queue"""
                    priority_queue.append((cost + neighbor_cost, neighbor, path + [node]))
            priority_queue = sorted(priority_queue, key=lambda x: x[0])

        """ Thuật toán GTS1"""

    def GTS1(self, start):
        # Tạo môt danh sách đã viến thăm rồi
        visited = set()
        stack = [start]
        # lưu lại đường đi
        tour = []
        cost = 0
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex) # ghi nhận đã đi qua
                tour.append(vertex) # và thêm vào tour
                node = None
                # Duyệt qua các hàn xóm
                for neighbor in self.vertices[vertex]:
                    if node == None and neighbor[0] not in visited:
                        node = neighbor
                    if neighbor[0] not in visited:
                        node =min([node, neighbor], key= lambda x:x[1])
                if node is not None:  # Thêm điều kiện kiểm tra
                    cost += node[1]
                    stack.append(node[0])
        if len(tour) == len(self.vertices):
            # Tìm kiếm điểm cuối cùng có nối với điểm đầu hay không
            for neighbor in self.vertices[tour[-1]]:
                if neighbor[0] == start:
                    cost+= neighbor[1]
                    tour.append(start)
                    return tour, cost
        return None, -1

    """ Thuật toán GTS2 """

    def GTS2(self, Vertice): # Vertic type list
        n=0
        tour = None
        cost = None
        while n < len(Vertice):
            start = Vertice[n]
            path, costVertice = self.GTS1(start)
            # trường hợp chưa có gì hết thì thêm chu trình mới vào
            if (tour == None  and path is not None):
                tour = path
                cost = costVertice
            if costVertice < cost:
                tour = path
                cost = costVertice
            n+=1
        return tour, cost







    # Hàm chuyển đổi ma trận thành đồ thị
    def convertMatrixToGraph(self, matrix):
        # Tạo các đỉnh trong đồ thị
        for i in range(len(matrix)):
            vertex = chr(ord('A') + i)  # Chuyển đổi thành ký tự A, B, C, ...
            self.add_vertex(vertex)

        # Tạo các cạnh trong đồ thị
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > 0:
                    vertex1 = chr(ord('A') + i)
                    vertex2 = chr(ord('A') + j)
                    cost = matrix[i][j]
                    self.add_edge(vertex1, vertex2, cost)


if __name__ == "__main__":

    # file_path = 'inputMatrix.txt'
    # # Đọc dữ liệu từ file văn bản và tạo thành một DataFrame
    # df = pd.read_csv(file_path, sep=',', header=None)
    # # Chuyển đổi DataFrame thành một ma trận NumPy
    # matrix = df.values
    # # Hiển thị ma trận
    # # ma trận này được lấy từ trong giá trình trang 61
    # print(matrix)
    # print("-----------------------------")
    # matrix =[[0,20,42,31,6,24],[10,0,17,6,35,18],[25,5,0,27,14,9]
    # ,[12,9,24,0,30,12],[14,7,21,15,0,38],[40,15,16,5,20,0]]

    matrix =[[0,28,36,34,10,29],[16,0,20,11,37,23],[17,9,0,32,18,13],
             [16,13,28,0,35,19],[18,14,25,19,0,49],[40,19,20,11,91,0]]
    graph = Graph()
    graph.convertMatrixToGraph(matrix)

  # Kiểm tra UCS
    start,end ="A","E"
    path, cost =graph.UCS(start, end)
    print("Kết quả của thuật toán UCS đi từ "+start+"-->"+end )
    print("Đường đi ngắn nhất", path)
    print("Chi phí thấp nhất",cost)
    print("-----------------------------------")

    # Kiểm tra hàm gts1
    print("Kết quả chạy thuật toán GTS1")
    start_vertex = "F"
    result, cost = graph.GTS1(start_vertex)
    if result is not None:
        print("Tìm thấy chu trình  : \n", result)
        print("Với chi phí là: ", cost)
    else:
        print("Không tìm thấy chu trình ")
    print("-----------------------------------")

    # Kiểm tra Thuật toán GTS2
    print("Kết quả chạy thuật toán GTS2")
    Vertice = ["A","C","D","F"]
    tour, cost =graph.GTS2(Vertice)
    print("Trong ba điểm ", Vertice )
    print(" Điểm có đường đi chi phí thấp nhất là : \n", tour)
    print("Với chi phí là ", cost)
    print("-------------------------------------")

