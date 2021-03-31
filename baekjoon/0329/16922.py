N = int(input())
result = [False] * 1001
# i = 1, j = 5, k = 10, N - (i+j+k) = 50 
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            Sum = 1 * i + 5 * j + 10 * k + 50 * (N-(i+j+k))
            result[Sum] = True
print(sum(result))