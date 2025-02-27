import queue
# đọc file từ dứ liệu trò chơi taci sau đó lấy ra hình dạng bắt đầu  và hình dạng kết thúc
def getTaci():
    taci = []
    f = open("taci.txt")
    for line in f.readlines():
        node = line.split()
        taci.append(node)
    f.close()
    return taci[:3],taci[3:]

def getHeuristics():
    heuristics = {}
    f = open("heuristics.txt")
    for i in f.readlines():
        node_heuristic_val = i.split()
        heuristics[node_heuristic_val[0]] = int(node_heuristic_val[1])
    f.close()
    return heuristics

# lấy dữ liệu file cities.txt
def getCity():
    city = {}
    citiesCode={}
    f = open('cities.txt')
    j = 1
    for i in f.readlines():
        node_city_val = i.split()
        city[node_city_val[0]] = [int(node_city_val[1]), int(node_city_val[2])]
        citiesCode[j] = node_city_val[0]
        j +=1
    f.close()
    return city,citiesCode


def createGraph():
    graph = {}
    file= open("citiesGraph.txt")
    for i in file.readlines():
        node_val = i.split()
        if node_val[0] in graph and node_val[1] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

        elif node_val [0] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0] : c})

            graph[node_val[1]] = [[node_val[0], node_val[2]]]

        elif node_val[1] in graph:
            c = graph.get(node_val [1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

            graph[node_val[0]] = [[node_val[1], node_val[2]]]
        else:
            graph[node_val[0]] = [[node_val[1], node_val[2]]]
            graph[node_val[1]] = [[node_val[0], node_val[2]]]
    file.close()
    return graph


def Astar(startNode, heuristics, graph, goalNode):
    priorityQueue = queue.PriorityQueue()  # Khởi tạo hàng đợi ưu tiên
    distance = 0  # Biến lưu tổng khoảng cách
    path = []  # Danh sách lưu các nút trên đường đi
    # Đặt nút khởi đầu vào hàng đợi ưu tiên với ưu tiên là tổng heuristic và khoảng cách
    priorityQueue.put((heuristics[startNode] + distance, [startNode, 0]))

    while not priorityQueue.empty():  # Lặp cho đến khi hàng đợi ưu tiên rỗng
        current = priorityQueue.get()[1]  # Lấy nút có ưu tiên cao nhất ra khỏi hàng đợi
        path.append(current[0])  # Thêm nút hiện tại vào danh sách các nút trên đường đi
        distance += int(current[1])  # Cộng thêm khoảng cách từ nút trước đến nút hiện tại

        if current[0] == goalNode:  # Nếu đã đạt được nút đích thì dừng
            break
        priorityQueue = queue.PriorityQueue()  # Khởi tạo hàng đợi ưu tiên mới

        # Duyệt qua các nút kề của nút hiện tại
        for i in graph[current[0]]:
            if i[0] not in path:  # Kiểm tra nút kề đã được xét trước đó hay chưa
                # Đặt nút kề vào hàng đợi ưu tiên với ưu tiên là tổng heuristic, khoảng cách và heuristic từ nút kề đến nút đích
                priorityQueue.put((heuristics[i[0]] + int(i[1]) + distance, i))
    print(priorityQueue)
    return path, distance  # Trả về danh sách các nút trên đường đi và tổng khoảng cách


def AKT(trang_thai_bat_dau, trang_thai_dich):
    def heuristic(trang_thai):
        # Hàm heuristic tính toán ước lượng khoảng cách từ trạng thái hiện tại đến trạng thái đích
        h = 0
        for i in range(3):
            for j in range(3):
                if trang_thai[i][j] == 'None':
                    continue
                x, y = divmod(int(trang_thai[i][j]) - 1, 3)
                h += abs(x - i) + abs(y - j)
        return h

    g = {str(trang_thai_bat_dau): 0}
    f = {str(trang_thai_bat_dau): heuristic(trang_thai_bat_dau)}
    # Khởi tạo các biến và cấu trúc dữ liệu

    open_list = [(f[str(trang_thai_bat_dau)], trang_thai_bat_dau)]
    path = []

    while open_list:
        _, state = open_list.pop(0)
        # Lấy trạng thái đầu tiên trong hàng đợi ưu tiên

        if state == trang_thai_dich:
            # Nếu trạng thái hiện tại là trạng thái đích, trả về đường đi và chi phí
            path = [state[i][j] for i in range(3) for j in range(3)]
            return path, g[str(state)]

        for i in range(3):
            for j in range(3):
                if state[i][j] == 'None':
                    x, y = i, j

        next_states = []

        # Tạo các trạng thái kế tiếp bằng cách hoán đổi vị trí ô 'None' với ô xung quanh

        if x > 0:
            next_state = [row[:] for row in state]
            next_state[x][y], next_state[x - 1][y] = next_state[x - 1][y], next_state[x][y]
            next_states.append(next_state)
        if x < 2:
            next_state = [row[:] for row in state]
            next_state[x][y], next_state[x + 1][y] = next_state[x + 1][y], next_state[x][y]
            next_states.append(next_state)
        if y > 0:
            next_state = [row[:] for row in state]
            next_state[x][y], next_state[x][y - 1] = next_state[x][y - 1], next_state[x][y]
            next_states.append(next_state)
        if y < 2:
            next_state = [row[:] for row in state]
            next_state[x][y], next_state[x][y + 1] = next_state[x][y + 1], next_state[x][y]
            next_states.append(next_state)

        # Duyệt qua các trạng thái kế tiếp và cập nhật chi phí và hàm ước lượng

        # Duyệt qua các trạng thái kế tiếp và cập nhật chi phí và hàm ước lượng

        for next_state in next_states:
            next_g = g[str(state)] + 1
            if str(next_state) not in g or next_g < g[str(next_state)]:
                g[str(next_state)] = next_g
                f[str(next_state)] = next_g + heuristic(next_state)
                open_list.append((f[str(next_state)], next_state))

        open_list.sort(key=lambda x: x[0])

    # Nếu không tìm được đường đi, trả về None
    return None, None


if __name__ == '__main__':
    heuristic = getHeuristics()

    graph = createGraph()

    print(heuristic)

    city, citiesCode = getCity()
    print(citiesCode)
    for i, j in citiesCode.items():
        print (i, j)
    start,goal = getTaci()
    print(start)
    print(goal)
    best,v = AKT(start,goal)
    print("Chạy thuật toán Akt")
    print(best)
    print(v)
    print("--------------------------------")
    print("chạy thuật toán A*")
    while True:
        inputCode1 = int(input("Nhập đỉnh bắt đầu: "))
        inputCode2 = int(input("Nhập đỉnh kết thúc: "))

        if inputCode1 == 0 or inputCode2 == 0:
            break
        startCity = citiesCode[inputCode1]
        endCity = citiesCode[inputCode2]
        print(startCity, endCity)

        astar,cost = Astar(startCity, heuristic, graph, endCity)
        print("ASTAR => ", astar,cost)