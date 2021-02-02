import sys

def cnt(n):
    if n == 1:
        return 1
    return n + cnt(n-1)
n = int(sys.stdin.readline())

for i in range(n):
    ox = sys.stdin.readline().rstrip().split('X')
    score = 0
    for j in ox:
        if 'O' in j:
            score += cnt(len(j))
    print(score)
        