# N-queen
def dfs(i):
    global cnt
    if i == N:
        cnt += 1
        return
    for j in range(N):
        if col[j] == 0 and diag_r[i+j] == 0 and diag_l[i-j] == 0:
            col[j] = 1
            diag_r[i+j] = 1
            diag_l[i-j] = 1
            dfs(i+1)
            col[j] = 0
            diag_r[i+j] = 0
            diag_l[i-j] = 0




N = int(input())

col = [0] * N
diag_r = [0] * (2 * N - 1)
diag_l = [0] * (2 * N - 1)

cnt = 0
dfs(0)
print(cnt)