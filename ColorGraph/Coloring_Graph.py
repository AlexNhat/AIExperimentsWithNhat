"""2186400330, LÊ Nguyễn ANh Nhật"""
# Thuật toán tô màu đồ thị bình thường
def ColorGraph(graph):
    # Tính bậc của các đỉnh trong đồ thị
    degrees = {vertex: len(graph[vertex]) for vertex in graph}
    # Sắp xếp các đỉnh theo thứ tự giảm dần của bậc
    order = sorted(degrees, key=degrees.get, reverse=True)
    # Khởi tạo một từ điển để lưu màu của các đỉnh
    colors = {}
    # Khởi tạo một danh sách các màu đã sử dụng
    used_colors = set()
    # Duyệt các đỉnh theo thứ tự đã sắp xếp
    for vertex in order:
        # Tìm các màu đã được sử dụng để tô các đỉnh kề trước đó
        used_colors.clear()
        for neighbor in graph[vertex]:
            if neighbor in colors:
                used_colors.add(colors[neighbor])
        # Tô đỉnh hiện tại bằng màu chưa được sử dụng trước đó (nếu có) hoặc một màu mới nếu không còn màu phù hợp để tô
        for color in range(1,len(order)):
            if color not in used_colors:
                colors[vertex] = color
                break
    return colors

# Tô màu tối ưu
def ColorGraphOptimization(graph):
    # Các đỉnh chưa có màu
    colors = {v: 0 for v in graph}
    # VÒng lặp kết thúc khi các đỉnh đều được tô màu
    while any(colors[v] == 0 for v in graph):
        # Tìm đỉnh có bậc lớn nhất
        max_degree_vertex = max([v for v in graph if colors[v] == 0], key=lambda v: len(graph[v]))
        # Tô màu cho đỉnh có bậc lớn nhất và cấm tô các đỉnh kề
        used_colors = {colors[v] for v in graph[max_degree_vertex] if colors[v] != 0}
        color = 1
        while color in used_colors:
            color += 1
        colors[max_degree_vertex] = color
    return colors

# TÔ màu tham lam
def GreedyColoringGraph(graph):
    colors = {v: 0 for v in graph}
    color = 1
    # n là số đỉnh đã được tô màu
    n=0
    for vertex in graph:
        # nếu đã được tô hết thì kết thúc
        if n ==(len(graph)):
            break
            # nếu điểm đã được tô thì bỏ qua
        if colors[vertex] !=0:
            pass
        # set chứa các màu đã được tô và tô màu cho đỉnh đãng xét
        PaintedVertices =set(graph[vertex])
        colors[vertex] = color
        n+=1
        # Vòng lặp làm công việc tham lam tô màu cho các đỉnh không kề
        for vertice in graph:
            if vertice not in PaintedVertices and colors[vertice]==0:
                colors[vertice] = color
                n+=1
                for ban in graph[vertice]:
                    PaintedVertices.add(ban)
        PaintedVertices.clear()
        color +=1
    return colors

# Tô màu sắp xếp tham lam
def GreedyOrderColoringGraph(graph):
    # Khởi tạo dict chứa màu của từng đỉnh ban đầu
    colors = {v: 0 for v in graph}
    #  Sắp xếp các đỉnh theo thứ tự giảm dần
    vertices = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
    color = 1
    # Duyệt từng đỉnh theo thứ tự đã sắp xếp
    for vertex in vertices:
        if colors[vertex] >0:
            continue
        # Tập các đỉnh cấm tô
        BanPaintedVertices = set(graph[vertex])
        colors[vertex] = color
        # dùng tham lam để tô màu
        for vertice in graph:
            if vertice not in BanPaintedVertices and colors[vertice] == 0:
                colors[vertice] = color
                # thêm các đỉnh cấm tô mới
                for ban in graph[vertice]:
                    BanPaintedVertices.add(ban)
        # xóa dữ liệu
        BanPaintedVertices.clear()
        color += 1

    return colors

def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            data = line.strip().split(':')
            vertex = data[0]
            edges = data[1].split(',') if len(data) > 1 else []
            graph[vertex] = [e.strip() for e in edges]
    return graph



if __name__== "__main__":

    graph = read_graph_from_file("input_color.txt")
    print("Dữ liệu có dạng: ")
    print(graph)
    NormalColorGraph = ColorGraph(graph)
    print("+ Sau khi dùng thuật toán tô màu thường ta đươc :\n ", NormalColorGraph)
    OptimizrColor = ColorGraphOptimization(graph)
    print("+ Sau khi dùng thuật toán tô màu tối ưu:\n ", OptimizrColor)
    GreedyColor = GreedyColoringGraph(graph)
    print("+ Sau khi dùng thuật toán tô màu tham lam: \n", GreedyColor)
    GreedyOrderColor = GreedyOrderColoringGraph(graph)
    print("+ Sau khi dùng thuật toán tô màu sắp xếp tham lam: \n", GreedyOrderColor)


