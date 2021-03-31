N, K, M = map(int, input().split())

q = []
for i in range(1, N+1):
    q.append(i)

cnt = 0

while q:
    for j in range(K-1):
        q.append(q.pop(0))
    tmp = q.pop(0)
    cnt += 1
    if tmp == M:
        break

print(cnt)
