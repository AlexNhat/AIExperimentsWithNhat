
from collections import defaultdict

def ReadFileTxt (file):
    size= int(file.readline())
    matrix = [[int (num) for num in line.split(' ')] for line in file] 
    return size, matrix

def convert_graph (a): 
    adjList=defaultdict(list) 
    for i in range (len(a)):
        adjList[i] = [] 
        for j in range (len (a[i])): 
            if a[i][j]==1: 
                adjList[i].append(j)   
    return adjList

#Colors_graphings
def color_graph(graph):
    sorted_vertices = sorted(graph, key=lambda v: -len(graph[v]))
    vertex_colors = {v: 0 for v in graph}
    for vertex in sorted_vertices:
        used_colors = {vertex_colors[v] for v in graph[vertex] if vertex_colors[v] != 0}
        color = 1
        while color in used_colors:
            color += 1
        vertex_colors[vertex] = color
    return vertex_colors

#Colors_optimization
def color_optimization(graph):
    vertex_colors = {v: 0 for v in graph}

    while any(vertex_colors[v] == 0 for v in graph):
        max_degree_vertex = max([v for v in graph if vertex_colors[v] == 0], key=lambda v: len(graph[v]))
        used_colors = {vertex_colors[v] for v in graph[max_degree_vertex] if vertex_colors[v] != 0}
        color = 1
        while color in used_colors:
            color += 1
        vertex_colors[max_degree_vertex] = color

    return vertex_colors

# Greedy_graphing
def greedy_coloring(graph):
    vertex_colors = {v: 0 for v in graph}
    for vertex in graph:
        used_colors = {vertex_colors[v] for v in graph[vertex] if vertex_colors[v] != 0}
        color = 1
        while color in used_colors:
            color += 1
        vertex_colors[vertex] = color
    return vertex_colors

#Greedy_best_vertex
def greedy_best_first_coloring(graph):
    vertex_colors = {v: 0 for v in graph}
    for vertex in sorted(graph, key=lambda v: sum(vertex_colors[w] != 0 for w in graph[v])):
        used_colors = {vertex_colors[v] for v in graph[vertex] if vertex_colors[v] != 0}
        color = 1
        while color in used_colors:
            color += 1
        vertex_colors[vertex] = color
    return vertex_colors


if __name__== "__main__":

    file = open("Input_color.txt","r")
    size, matrix = ReadFileTxt(file)
    file.close()
    graph = convert_graph(matrix)
    
    result_colorR = color_graph(graph)
    print("Kết quả sử dụng thuật toán tô màu đồ thị: \n",result_colorR)
    result_colorO = color_optimization(graph)
    print("Kết quả sử dụng thuật toán tô màu tối ưu: \n",result_colorO)

    result_greedyR = greedy_coloring(graph)
    print("Kết quả sử dụng thuật toán tô màu tham lam: \n",result_greedyR)
    result_GBFC = greedy_best_first_coloring(graph)
    print("Kết quả sử dụng thuật toán tô màu tham lam + tối ưu: \n",result_GBFC)

