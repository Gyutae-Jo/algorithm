def bfs(idx, cnt):
    global MAX
    visited[idx] = 1
    if cnt > MAX:
        MAX = cnt
    for j in range(1, N+1):
        if adj[idx][j] and visited[j] == 0:
            bfs(j, cnt + 1)
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        i, j = map(int, input().split())
        adj[i][j] = 1
        adj[j][i] = 1
    MAX = 1
    for k in range(1, N):
        visited = [0] * (N+1)
        bfs(k, 1)
    print(f'#{tc} {MAX}')