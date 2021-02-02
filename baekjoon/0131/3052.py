import sys

result = []

for i in range(10):
    result.append(int(sys.stdin.readline())%42)

print(len(set(result)))