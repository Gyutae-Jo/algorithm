import sys

n = int(sys.stdin.readline())

for i in range(n):
    a=sys.stdin.readline().split()

    print(f'Case #{i+1}:',int(a[0])+int(a[-1]))

