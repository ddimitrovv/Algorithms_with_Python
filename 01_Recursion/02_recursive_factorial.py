def recursive_factorial(num):

    if num <= 1:
        return 1
    result = num * recursive_factorial(num - 1)
    return result


num = int(input())
print(recursive_factorial(num))
