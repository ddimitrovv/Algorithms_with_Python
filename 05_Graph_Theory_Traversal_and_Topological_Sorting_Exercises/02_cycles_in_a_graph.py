def dfs(graph, node, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return

    visited.append(node)
    cycles.append(node)

    for child in graph[node]:
        dfs(graph, child, visited, cycles)

    cycles.remove(node)


graph = {}

while True:
    line = input()
    if line == 'End':
        break

    key, value = line.split('-')
    if key not in graph:
        graph[key] = []
    if value not in graph:
        graph[value] = []
    graph[key].append(value)

try:
    visited = []
    for node in graph:
        dfs(graph, node, visited, [])
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
