def summation(n):
    if n == 1:
        return 1
    return n + summation(n-1)

n = int(input())

print(summation(n))