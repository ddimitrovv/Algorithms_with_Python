numbers = [int(x) for x in input().split()]

for idx in range(len(numbers)):
    min_idx = idx

    for next_idx in range(idx + 1, len(numbers)):
        min_num = numbers[idx]
        if numbers[next_idx] < min_num:
            min_idx = next_idx
            min_num = numbers[next_idx]
            numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

print(*numbers)
