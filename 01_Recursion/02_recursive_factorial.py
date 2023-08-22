cached = {}


def recursive_factorial(num):
    if num in cached:
        return cached[num]
    if num <= 1:
        cached[num] = 1
        return 1
    result = num * recursive_factorial(num - 1)
    if num in cached:
        return cached[num]
    cached[num] = result
    return result


num = int(input())
print(recursive_factorial(num))
# print(cached)
