cache = {}


def get_fibonacci(num):
    if num <= 1:
        return 1
    if num in cache:
        return cache[num]
    result = get_fibonacci(num - 1) + get_fibonacci(num - 2)
    cache[num] = result
    return result
    # return get_fibonacci(num - 1) + get_fibonacci(num - 2)


number = int(input())
print(get_fibonacci(number))
