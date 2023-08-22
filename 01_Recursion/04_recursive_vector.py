def generate(idx, vect):
    if idx >= len(vect):
        print(*vect, sep='')
        return
    for num in range(2):
        vect[idx] = num
        generate(idx + 1, vect)


n = int(input())
vector = [0] * n

generate(0, vector)
