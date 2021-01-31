import sys

n = int(sys.stdin.readline())

for i in range(n):
    scores = list(map(int, sys.stdin.readline().split()))
    avg = sum(scores[1:]) / scores[0]
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1
    print('{:.3f}%'.format(cnt/scores[0]*100))