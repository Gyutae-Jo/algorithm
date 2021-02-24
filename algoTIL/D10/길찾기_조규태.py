
for k in range(10):
    tc, E = map(int, input().split())
    edge = list(map(int, input().split()))
    arr = [[0 for _ in range(100)] for _ in range(100)]
    # edge 경로를 2차원 배열에 표시
    for i in range(len(edge)//2):
        arr[edge[i*2]][edge[i*2+1]] = 1

    stack = [0]*100
    top = -1
    visited = [0]*100

    top += 1
    stack[top] = 0

    # 99에 도착하면 1 도착못하면 0
    result = 0
    while top >= 0:
        # 현재 top에 있는 원소 꺼내기기
        cur = stack[top]
        top -= 1
        if visited[cur] == 0:
            visited[cur] = 1

            for i in range(100):
                if arr[cur][i] == 1 and visited[i] != 1:
                    top += 1
                    stack[top] = i
                    if i == 99:
                        result = 1
    print(f'#{tc} {result}')

