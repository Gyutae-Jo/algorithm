n = int(input())
arr = [list(input()) for _ in range(n)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(i, j):
    q = []
    # 단지 내 집 개수
    cnt = 0
    q.append((i,j))
    arr[i][j] = 0
    cnt += 1
    while q:
        tmp = q.pop(0)
        nr = tmp[0]
        nc = tmp[1]
        for i in range(4):
            if 0 <= nr + dr[i] < n and 0 <= nc + dc[i] < n:
                if arr[nr + dr[i]][nc + dc[i]] == '1':
                    q.append((nr+dr[i], nc+dc[i]))
                    arr[nr + dr[i]][nc + dc[i]] = 0
                    cnt += 1
    result.append(cnt)

result = []
# 단지 갯수
count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            count += 1
            bfs(i, j)
print(count)
result.sort()
for k in result:
    print(k)
