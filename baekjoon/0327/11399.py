N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
result = 0
for n in range(1, N+1):
    for i in range(n):
        result += arr[i]
print(result)