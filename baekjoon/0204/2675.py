import sys
n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().split()
    for j in s[1]:
        print(f'{j*int(s[0])}', end="")
    print()
