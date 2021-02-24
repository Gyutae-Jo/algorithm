def Sum(N):
    if N == 1:
        return 1
    return N + Sum(N-1)

print(Sum(10))