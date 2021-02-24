arr = [list(map(int, input().split())) for _ in range(5)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(5):
    for j in range(5):
        Sum = 0
        for k in range(4):
            if 0 <= i+dr[k] < 5 and 0 <= j+dc[k] < 5:
                Sum += abs(arr[i+dr[k]][j+dc[k]]-arr[i][j])
        print(Sum, end=" ")
    print()
