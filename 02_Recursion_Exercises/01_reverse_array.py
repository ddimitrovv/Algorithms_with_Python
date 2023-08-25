def reverse_array(numbers, idx):
    if len(numbers) // 2 == idx:
        print(' '.join(numbers))
        return
    numbers[idx], numbers[len(numbers) - 1 - idx] = numbers[len(numbers) - 1 - idx], numbers[idx]
    reverse_array(numbers, idx + 1)


arr = input().split()
reverse_array(arr, 0)
