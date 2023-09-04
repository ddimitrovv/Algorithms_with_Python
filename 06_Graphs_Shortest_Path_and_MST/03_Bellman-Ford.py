from collections import deque


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


count_nodes = int(input())
count_edges = int(input())

graph = []

for _ in range(count_edges):
    start, end, weight = [int(x) for x in input().split(' ')]
    graph.append(Edge(start, end, weight))

start_node = int(input())
end_node = int(input())

distance = [float('inf')] * (count_nodes + 1)
parent = [None] * (count_nodes + 1)
distance[start_node] = 0

for _ in range(count_nodes - 1):
    for edge in graph:
        if distance[edge.start] == float('inf'):
            print(edge.start)
