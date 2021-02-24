T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N-K+1):
            if N==K:
                # 행에 대해서
                Sum = 0
                for k in range(j, j+K):
                    Sum += arr[i][k]
                if Sum == K:
                    cnt += 1
                # 열에 대해서
                Sum = 0
                for k in range(j, j+K):
                    Sum += arr[k][i]
                if Sum == K:
                    cnt += 1
            else:
                if j == 0:
                    # 행에 대해서
                    Sum = 0
                    for k in range(K):
                        Sum += arr[i][k]
                    if Sum == K and arr[i][K] == 0:
                        cnt += 1
                    # 열에 대해서
                    Sum = 0
                    for k in range(K):
                        Sum += arr[k][i]
                    if Sum == K and arr[K][i] == 0:
                        cnt += 1
                elif j==N-K:
                    # 행에 대해서
                    Sum = 0
                    for k in range(j, j + K):
                        Sum += arr[i][k]
                    if Sum == K and arr[i][j-1] == 0:
                        cnt += 1
                    # 열에 대해서
                    Sum = 0
                    for k in range(j, j + K):
                        Sum += arr[k][i]
                    if Sum == K and arr[j-1][i] == 0:
                        cnt += 1
                else:
                    # 행에 대해서
                    Sum = 0
                    for k in range(j, j + K):
                        Sum += arr[i][k]
                    if Sum == K and arr[i][j-1] == 0 and arr[i][j+K] == 0:
                        cnt += 1
                    # 열에 대해서
                    Sum = 0
                    for k in range(j, j + K):
                        Sum += arr[k][i]
                    if Sum == K and arr[j-1][i] == 0 and arr[j+K][i] == 0:
                        cnt += 1
    print(f'#{tc} {cnt}')