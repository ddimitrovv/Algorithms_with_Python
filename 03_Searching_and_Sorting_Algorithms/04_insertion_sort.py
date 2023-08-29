numbers = [int(x) for x in input().split()]

for i in range(1, len(numbers)):
    for j in range(i, 0, -1):
        if numbers[j] < numbers[j - 1]:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]

print(*numbers)
