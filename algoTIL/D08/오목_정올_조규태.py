# 19x19 입력 받기
arr = [list(map(int, input().split())) for _ in range(19)]
# 우 대각왼쪽아래 하 대각오른쪽아래
dr = [0, 1, 1, 1]
dc = [1, -1, 0, 1]
# breakpoint
bp = False
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            for k in range(len(dr)):
                a = i
                b = j
                cnt = 0
                while True:
                    if 0 <= a+dr[k] < 19 and b+dc[k] < 19:
                        a += dr[k]
                        b += dc[k]
                        if arr[a][b] == 1:
                            cnt += 1
                        if cnt == 5:
                            if 0 <= a + dr[k] < 19 and b + dc[k] < 19:
                                a += dr[k]
                                b += dc[k]
                                if arr[a][b] == 1:
                                    # cnt 가 6이므로 아님
                                    pass
                                else:
                                    pass
                                    # 1과 이때의 ij를 출력
                            else:
                                pass
                                # 1과 이때의 ij를 출력
                    else:
                        break
