N = int(input())
arr = []
for _ in range(N):
    n = int(input())
    arr.append(n)

# 선택정렬
for i in range(N-1):
    Min = i
    for j in range(i+1, N):
        if arr[Min] > arr[j]:
            Min = j
    arr[Min], arr[i] = arr[i], arr[Min]

for i in range(N):
    print(arr[i])