def sorted_nodes(graph, predecessors, output):
    while predecessors:
        nodes_to_remove = [k for k in predecessors if predecessors[k] == 0]
        if not nodes_to_remove:
            return False
        node_to_remove = nodes_to_remove[0]
        del predecessors[node_to_remove]
        output.append(node_to_remove)
        for child in graph[node_to_remove]:
            predecessors[child] -= 1

    return True


n = int(input())

graph = {}
for _ in range(n):
    key, value = input().split(' ->')
    graph[key] = list(value.strip().split(', ')) if value and value != ' ' else []

predecessors = {}

for node, children in graph.items():
    if node not in predecessors:
        predecessors[node] = 0
    for child in children:
        if child not in predecessors:
            predecessors[child] = 1
        else:
            predecessors[child] += 1

output = []

is_sortable = sorted_nodes(graph, predecessors, output)
if is_sortable:
    print(f'Topological sorting: {", ".join(str(x) for x in output)}')
else:
    print('Invalid topological sorting')
