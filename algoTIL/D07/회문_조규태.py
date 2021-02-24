T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Str = [list(input()) for _ in range(N)]
    tmp_r = ""
    tmp_c = ""
    for i in range(N):
        for j in range(N-M+1):
            tmp_r = ""
            tmp_c = ""
            for k in range(j, j+M):
                tmp_r += Str[i][k]
                tmp_c += Str[k][i]
            if tmp_r == tmp_r[::-1] or tmp_c == tmp_c[::-1]:
                break
        if tmp_r == tmp_r[::-1]:
            print(f'#{tc} {tmp_r}')
            break
        elif tmp_c == tmp_c[::-1]:
            print(f'#{tc} {tmp_c}')
            break