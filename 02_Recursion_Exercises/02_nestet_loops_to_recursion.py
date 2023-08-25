def nested_loops(idx, numbers):
    if idx >= len(numbers):
        print(*numbers, sep=' ')
        return
    for num in range(1, len(numbers) + 1):
        numbers[idx] = num
        nested_loops(idx + 1, numbers)


n = int(input())
arr = [None] * n
nested_loops(0, arr)
