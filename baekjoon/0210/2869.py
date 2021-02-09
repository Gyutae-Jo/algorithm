import sys
A, B, V = map(int, sys.stdin.readline().split())
h = 0
day = 0
if (V-A)%(A-B)==0:
    print((V-A)//(A-B)+1)
elif (V-A)%(A-B) != 0:
    print((V-A)//(A-B)+2)
