def merge_arrs(left, right):
    new_array = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            new_array.append(left[left_idx])
            left_idx += 1
        else:
            new_array.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        new_array.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        new_array.append(right[right_idx])
        right_idx += 1

    return new_array


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    middle = len(nums) // 2
    return merge_arrs(merge_sort(nums[:middle]), merge_sort(nums[middle:]))


numbers = [int(x) for x in input().split()]
sorted_array = merge_sort(numbers)
print(*sorted_array)
