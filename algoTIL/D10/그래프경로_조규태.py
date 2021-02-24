T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        arr[i][j] = 1
        # arr[j][i] = 1

    S, G = map(int, input().split())

    s = [0] * V
    top = -1
    visted = [0] * (V+1)

    top += 1
    s[top] = S
    result = 0
    while top >= 0:
        cur = s[top]
        top -= 1

        if visted[cur] == 0:
            visted[cur] = 1

            for i in range(1, V+1):
                if arr[cur][i] == 1 and visted[i] == 0:
                    top += 1
                    s[top] = i
                    if i == G:
                        result = 1
    print(f'#{tc} {result}')