def dfs(node, graph, visited, node_salary):
    if visited[node]:
        return node_salary[node]

    visited[node] = True

    if not graph[node]:
        node_salary[node] = 1
        return node_salary[node]

    if node not in node_salary:
        node_salary[node] = 0

    for child in graph[node]:
        node_salary[node] += dfs(child, graph, visited, node_salary)

    return node_salary[node]


count_nodes = int(input())
graph = {}

for key in range(count_nodes):
    graph[key] = [node for node, child in enumerate(list(input())) if child == 'Y']

sum_salaries = 0
node_salary = {}
visited = [False] * len(graph)

for node in graph:
    sum_salaries += dfs(node, graph, visited, node_salary)

print(sum_salaries)
