# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if 0 <= i + dr[k] < N and 0 <= j + dc[k] < N:
                    if arr[i + dr[k]][j + dc[k]] - arr[i][j] == 1:
                        cnt[arr[i][j]] = 1
    cnt_sum = [0] * len(cnt)
    for j in range(len(cnt)-1, 0, -1):
        if j == len(cnt) - 1:
            cnt_sum[j] = cnt[j]
        else:
            if cnt[j]:
                cnt_sum[j] = cnt[j] + cnt_sum[j+1]

    MAX = max(cnt_sum)
    idx = cnt_sum.index(max(cnt_sum))

    print(f'#{tc} {idx} {MAX+1}')