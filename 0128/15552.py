import sys
import time

n = int(sys.stdin.readline())

for i in range(n):
    a=sys.stdin.readline().split()
    start = time.time()
    # print(eval(a[0]+'+'+a[-1])) # 이 코드로 print하면 시간초과 뜸
    print(int(a[0])+int(a[-1]))

    print("time:",time.time() - start)
