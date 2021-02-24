T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0

    for i in range(N-M+1):

        for j in range(N-M+1):
            Sum = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    Sum += arr[k][l]

            if Sum > Max:
                Max = Sum
    print(f'#{tc} {Max}')
