N, M = map(int, input().split())
checked = [False] * N
arr = []

def perm(depth, N, M):
    if depth == M:
        print(" ".join(map(str,arr)))
        return
    else:
        for i in range(len(checked)):
            if not checked[i]:
                checked[i] = True
                arr.append(i+1)
                perm(depth+1, N, M)
                checked[i] = False
                arr.pop()

perm(0, N, M)
