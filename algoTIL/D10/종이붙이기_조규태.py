def dfs(N):
    global memo
    if N >= 3 and len(memo) <= N:
        memo.append(dfs(N-1)+dfs(N-2)*2)
    return memo[N]

# 길이가 0일때 0, 길이가 1일때 ㅣ 모양 1개, 길이가 2일때 ㅣㅣ, ㅁ, = 이렇게 3개
memo = [0, 1, 3]

T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    dfs(N)

    print(f'#{tc} {dfs(N)}')

# def dfs(N):
#     if N == 0:
#         global cnt
#         cnt += 1
#     else:
#         for i in range(3):
#             if N - arr[i] >= 0:
#                 dfs(N - arr[i])
#
# # ㅣ, ㅁ, = 이렇게 3개의 모양의 도형이 있다. 길이는 각각 10, 20, 20
# arr = [10, 20, 20]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cnt = 0
#     dfs(N)
#     print(f'#{tc} {cnt}')