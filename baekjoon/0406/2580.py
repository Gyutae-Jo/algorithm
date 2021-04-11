arr = list(map(int, input().split()) for _ in range(9))
# 
a = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            a.append([i,j])

for k in range(len(a)):
    nr = a[k][0]
    nc = a[k][1]
    # 가로 9개 검사
    a[k].append(arr[nr].find(0))

    # 세로 9개 검사
    cnt = 0
    for l in range(9):
        if arr[l][nc] == 0:
            cnt += 1
    if a[k][2] > cnt


    for l in range(4):
        while True:

