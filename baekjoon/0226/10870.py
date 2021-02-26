def fibo(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fibo(N-1) + fibo(N-2) 

N = int(input())
print(fibo(N))