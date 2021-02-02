import sys

def hansu(n):
    if n<100:
        return True
    while n != 0:
        n1 = n % 10
        n //= 10
        n2 = n % 10
        n //= 10
        n3 = n % 10
        n //= 10
        if n1 - n2 != n2 - n3:
            return False
    return True

n = int(sys.stdin.readline())

cnt = 0
for i in range(1, n+1):
    cnt += hansu(i)
print(cnt)