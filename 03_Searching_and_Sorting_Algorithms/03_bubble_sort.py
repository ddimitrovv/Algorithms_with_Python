numbers = [int(x) for x in input().split()]

# for i in range(len(numbers)):
#     for j in range(1, len(numbers) - i):
#         if numbers[j - 1] > numbers[j]:
#             numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
#
# print(*numbers)

is_sorted = False
i = 0

while not is_sorted:
    is_sorted = True
    for j in range(1, len(numbers) - i):
        if numbers[j - 1] > numbers[j]:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
            is_sorted = False
    i += 1

print(*numbers)