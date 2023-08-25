def find_paths(row, col, direction, labyrinth, path):
    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[0]):
        return

    if labyrinth[row][col] == '*':
        return

    if labyrinth[row][col] == 'v':
        return

    path.append(direction)

    if labyrinth[row][col] == 'e':
        print(''.join(path))
    else:
        labyrinth[row][col] = 'v'
        find_paths(row, col + 1, 'R', labyrinth, path)
        find_paths(row, col - 1, 'L', labyrinth, path)
        find_paths(row + 1, col, 'D', labyrinth, path)
        find_paths(row - 1, col, 'U', labyrinth, path)
        labyrinth[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())
labyrinth = []
for _ in range(rows):
    labyrinth.append(list(input()))

find_paths(0, 0, '', labyrinth, [])
