T = int(input())
for tc in range(1, T+1):
    N = int(input())
    boxTop = list(map(int, input().split()))
    room = [[0 for _ in range(100)] for _ in range(N)]
    for  i in range(N):
        for j in range(boxTop[i]):
            room[i][j] = 1

    Max = 0
    for i in range(N):
        if boxTop[i] > 0:
            dist = 0
            for j in range(i+1, N):
                if room[j][boxTop[i]-1] == 0:
                    dist += 1
            if Max < dist:
                Max = dist
    print("#{} {}".format(tc, Max))

