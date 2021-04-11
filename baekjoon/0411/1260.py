def dfs(v):
    print(v, end=" ")
    visited[v] = 1
    for j in range(1, N+1):
        if arr[v][j] == 1 and visited[j] == 0:
            dfs(j)

def bfs(v):
    V = [0] * (N+1)
    q = []
    q.append(v)
    V[v] = 1
    while q:
        tmp = q.pop(0)
        print(tmp, end=" ")
        for i in range(1, N+1):
            if arr[tmp][i] == 1 and V[i] == 0:
                q.append(i)
                V[i] = 1


N, M, V = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
visited = [0] * (N+1)
stack = []
dfs(V)
print()
bfs(V)