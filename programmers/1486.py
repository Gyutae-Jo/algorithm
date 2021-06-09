def dfs(idx, tmp_h):
    global MIN
    if idx == N or tmp_h >= B:
        if tmp_h < B:
            return
        if tmp_h - B < MIN:
            MIN = tmp_h - B
        return
    check[idx] = 1
    dfs(idx+1, tmp_h + H[idx])
    check[idx] = 0
    dfs(idx+1, tmp_h)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    # 최악의 경우 모든 점원의 키를 다 더해야 할수도
    MIN = sum(H) - B
    check = [0] * len(H)
    dfs(0, 0)
    print(f'#{tc} {MIN}')
