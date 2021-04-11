T = int(input())

coord = []
for _ in range(T):
    x, y = map(int, input().split())
    coord.append((x, y))
coord.sort(key = lambda x : (x[0], x[1]))
for i in range(T):
    print(coord[i][0], coord[i][1])