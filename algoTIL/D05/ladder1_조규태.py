# 상하좌우 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for _ in range(10):
    tc = int(input())
    # input 이차원 array
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 시작 행
    i = 99
    # 시작 열
    j = -1
    for k in range(100):
        if arr[99][k] == 2:
            j = k
            break

    # 지나온 막대로 다시 가는 것을 막기 위한 숫자 직전에 좌로 갔으면 0 우로 갔으면 1 위로 갔으면 -1
    p = -1
    # 사다리 거꾸로 올라가기 시작
    while True:
        # 제일 왼쪽 막대일때
        if j == 0: # 왼쪽으로는 이동못함
            # 오른쪽에 막대있고 p가 0이 아니면 우로 이동
            # p를 확인하는 건 좌우로만 이동하는걸 방지하기 위해
            if arr[i][j+dc[3]] == 1 and p != 0:
                i += dr[3]
                j += dc[3]
                p = 1
            else: # 위로 올라가는 상황
                if i == 0: # 이때의 j가 답
                    break
                else:
                    i += dr[0]
                    j += dc[0]
                    p = -1
        # 제일 오른쪽 막대일때
        elif j == 99:
            if arr[i][j+dc[2]] == 1 and p != 1:
                i += dr[2]
                j += dc[2]
                p = 0
            else: # 위로 올라가는 상황
                if i == 0: # 이때의 j가 답
                    break
                else:
                    i += dr[0]
                    j += dc[0]
                    p = -1
        else:
            if arr[i][j+dc[3]] == 1 and p != 0: # 오른쪽으로 이동
                i += dr[3]
                j += dc[3]
                p = 1
            elif arr[i][j+dc[2]] == 1 and p != 1: # 왼쪽이동
                # p 조건은 왔던길로 다시 안가기 위해
                i += dr[2]
                j += dc[2]
                p = 0
            else: # 위로 올라가는 상황
                if i == 0: # 이때의 j가 답
                    break
                else:
                    i += dr[0]
                    j += dc[0]
                    p = -1
    print(f'#{tc} {j}')


