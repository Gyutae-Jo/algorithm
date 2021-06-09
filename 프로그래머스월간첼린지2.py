a = [-5, 0, 2, 1, 2]
edges = [[0, 1], [3, 4], [2, 3], [0, 3]]
# result = 9
# a = [0, 1, 0]
# b = [[0, 1], [1, 2]]
# result =  -1


count = 0


def in_order(node, p_node, tree):
    global count
    if node:
        in_order(tree[node][0], node, tree)
        in_order(tree[node][2], node, tree)
        if p_node:
            while tree[node][1] < 0:
                tree[node][1] += 1
                tree[p_node][1] -= 1
                count += 1
            while tree[node][1] > 0:
                tree[node][1] -= 1
                tree[p_node][1] += 1
                count += 1



def solution(a, edges):
    # 정점개수
    n  = len(a)
    tree = [[0] * 3 for _ in range(n+1)]
    
    for edge in edges:
        p, c = edge
        p += 1
        c += 1
        if p == 1:
            pass
        elif c == 1:
            p, c = c, p
        else:
            cnt = 0
            for ed in edges:
                if c-1 in ed:
                    cnt += 1
            if cnt == 1:
                pass
            else:
                p, c = c, p

        if not tree[p][0]:
            tree[p][0] = c
            
        else:
            tree[p][2] = c
    for i in range(n):
        tree[i+1][1] = a[i]

    in_order(1, 0, tree)
    flag = True
    for i in range(1, n+1):
        if tree[i][1]:
          flag=False
          break
    if flag:
        print(count)
        return count
    else:
        print(-1)
        return -1

solution(a, edges)
