# def p_c_decision(a, b):
#     if a == 1:
#         return a, b
#     if b == 1:
#         return b, a
#     for branch in tree:
#         if branch[0] == a or branch[2] == a:
#             return a, b
#         if branch[0] == b or branch[2] == b:
#             return b, a
#     return a, b
import sys
input = sys.stdin.readline
N = int(input())

# tree = [[0]*3 for _ in range(N+1)]

# for i in range(N-1):
#     a, b = map(int, input().split())
#     p, c = p_c_decision(a, b)
#     if tree[p][0] == 0:
#         tree[p][0] = c
#         tree[c][1] = p
#     else:
#         tree[p][2] = c
#         tree[c][1] = p

# for j in range(2, N+1):
#     print(tree[j][1])

visited = [0]*(N+1)
for i in range(N-1):
    a, b = map(int, input().split())
    if a == 1:
        visited[b] = a
    elif b == 1:
        visited[a] = b
    elif not visited[a]:
        visited[a] = b
    elif not visited[b]:
        visited[b] = a
for i in range(2, N+1):
    print(visited[i])