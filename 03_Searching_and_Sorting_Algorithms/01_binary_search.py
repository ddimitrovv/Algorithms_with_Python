def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_num = numbers[mid_idx]

        if target == mid_num:
            return mid_idx

        if mid_num > target:
            right = mid_idx - 1
        else:
            left = mid_idx + 1

    return -1


numbers = [int(x) for x in input().split()]
target = int(input())

print(binary_search(numbers, target))
