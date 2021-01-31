import sys

n = int(sys.stdin.readline())

scores = list(map(int, sys.stdin.readline().split()))
avg = sum(scores)/len(scores)
new_avg = avg/max(scores)*100
print(new_avg)
new_scores = [i/max(scores)*100 for i in scores]

print(sum(new_scores)/len(new_scores))