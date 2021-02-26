N = int(input())
result = 0
for i in range(N):
    tmp = i
    Sum = i
    while tmp != 0:
        Sum += (tmp % 10)
        tmp //= 10
    if Sum == N:
        result = i
        break
print(result)