def find_all_areas(row, col, rows, cols, matrix):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0
    if matrix[row][col] == '*':
        return 0
    if matrix[row][col] == 'v':
        return 0

    size_area = 1
    matrix[row][col] = 'v'

    size_area += find_all_areas(row + 1, col, rows, cols, matrix)
    size_area += find_all_areas(row - 1, col, rows, cols, matrix)
    size_area += find_all_areas(row, col + 1, rows, cols, matrix)
    size_area += find_all_areas(row, col - 1, rows, cols, matrix)

    return size_area


rows = int(input())
cols = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
positions = []

for row in range(rows):
    for col in range(cols):
        size = find_all_areas(row, col, rows, cols, matrix)
        if size != 0:
            positions.append((row, col, size))

print(f'Total areas found: {len(positions)}')

sorted_positions = sorted(positions, key=lambda x: -x[2])
for idx, position in enumerate(sorted_positions):
    print(f'Area #{idx + 1} at ({position[0]}, {position[1]}), size: {position[2]}')


