N = int(input())
arr = []
for i in range(N):
    w_h = list(map(int, input().split()))
    arr.append(w_h)
for i in range(len(arr)):
    index = []
    cnt = 0
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0]:
            index.append(j)
    for k in index:
        if arr[i][1] < arr[k][1]:
            cnt += 1
    print(cnt+1, end=" ")

