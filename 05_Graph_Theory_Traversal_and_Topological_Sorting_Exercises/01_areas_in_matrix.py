def dfs(curr_node, row, col, matrix, visited, result):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if visited[row][col]:
        return 0
    if matrix[row][col] != curr_node:
        return 0

    visited[row][col] = True
    dfs(curr_node, row - 1, col, matrix, visited, result)
    dfs(curr_node, row + 1, col, matrix, visited, result)
    dfs(curr_node, row, col - 1, matrix, visited, result)
    dfs(curr_node, row, col + 1, matrix, visited, result)

    return 1


rows = int(input())
cols = int(input())

matrix = [list(input()) for _ in range(rows)]
visited = [[False] * cols for _ in range(rows)]

result = {}

total_areas = 0
for row in range(rows):
    for col in range(cols):
        curr_node = matrix[row][col]
        value = dfs(curr_node, row, col, matrix, visited, result)
        total_areas += value

        if curr_node not in result:
            result[curr_node] = 0
        result[curr_node] += value


print(f'Areas: {total_areas}')
[print(f"Letter '{k}' -> {v}") for k, v in sorted(result.items())]
# for k, v in result.items():
#     print(f"Letter '{k}' -> {v}")
