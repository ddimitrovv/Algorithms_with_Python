from collections import deque

count_nodes = int(input())
count_edges = int(input())
graph = [[] for _ in range(count_nodes + 1)]

for _ in range(count_edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
end_node = int(input())

visited = [False] * (count_nodes + 1)
parent = [None] * (count_nodes + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()

    if node == end_node:
        break

    for child in graph[node]:
        if visited[child]:
            continue

        visited[child] = True
        queue.append(child)
        parent[child] = node


path = deque()
node = end_node

while node:
    path.appendleft(node)
    node = parent[node]

print(f'Shortest path length is: {len(path) - 1}')
print(*path)
