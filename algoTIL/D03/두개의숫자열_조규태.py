T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Max = 0
    if N > M:
        for i in range(N-M+1):
            ADD = 0
            for j in range(M):
                ADD += B[j] * A[j+i]
            if ADD > Max:
                Max = ADD
    else:
        for i in range(M-N+1):
            ADD = 0
            for j in range(N):
                ADD += A[j] * B[j+i]
            if ADD > Max:
                Max = ADD
    print(f'#{tc} {Max}')