def quicksort(nums, start_idx, end_idx):
    if start_idx >= end_idx:
        return

    pivot = start_idx
    left = pivot + 1
    right = end_idx

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]
    quicksort(nums, start_idx, right - 1)
    quicksort(nums, right + 1, end_idx)


numbers = [int(x) for x in input().split()]
quicksort(numbers, 0, len(numbers) - 1)
print(*numbers)


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     return quick_sort(left) + middle + quick_sort(right)
#
#
# # Example usage
# numbers = [int(x) for x in input().split()]
# sorted_list = quick_sort(numbers)
# print(*sorted_list)
