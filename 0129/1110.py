import sys

n = int(sys.stdin.readline())
cnt = 0
result = n
while True:
    if n < 10:
        n = n * 10 + n
        cnt += 1
        if n == result:
            print(cnt)
            break
    n = (n%10)*10 + (n//10 + n%10)%10
    cnt += 1
    if n == result:
        print(cnt)
        break