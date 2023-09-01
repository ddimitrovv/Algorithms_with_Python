def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)


count_nodes = int(input())
edges = int(input())

graph = {}
all_edges = []

for _ in range(edges):
    source, destination = [int(x) for x in input().split(' - ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []

    graph[source].append(destination)
    graph[destination].append(source)
    all_edges.append((min(source, destination), max(source, destination)))


removed_edges = []

print('Important streets:')
for source, destination in all_edges:
    graph[source].remove(destination)
    graph[destination].remove(source)

    visited = [False] * count_nodes
    dfs(0, graph, visited)

    if not all(visited):
        print(f'{source} {destination}')

    graph[source].append(destination)
    graph[destination].append(source)
