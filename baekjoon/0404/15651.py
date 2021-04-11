N, M = map(int, input().split())
arr = []

def perm(depth, N, M):
    if depth == M:
        print(" ".join(map(str,arr)))
        return
    else:
        for i in range(N):
            arr.append(i+1)
            perm(depth+1, N, M)
            arr.pop()

perm(0, N, M)
