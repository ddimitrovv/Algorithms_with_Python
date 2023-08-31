def dfs(node, visited, graph, connected):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, visited, graph, connected)

    connected.append(node)


n = int(input())
graph = {}

for i in range(n):
    graph[i] = [int(x) for x in input().split()]

visited = [False] * n

for node in graph:
    if visited[node]:
        continue
    connected = []
    dfs(node, visited, graph, connected)
    print(f'Connected component: {" ".join(str(x) for x in connected)}')
