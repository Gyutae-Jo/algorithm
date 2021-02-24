T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0 # N개의 원소를 갖고 원소의 합이 K인 부분집합의 개수
    for i in range(1<<12):
        n = 0 # 원소의 개수를 카운트
        k = 0 # 원소의 합
        for j in range(12):
            if i & (1<<j):
                n += 1
                k += (j+1)
        # print(n, k)
        if n == N and k == K:
            result += 1
    print(f'#{tc} {result}')