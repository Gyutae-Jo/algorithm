import sys
n1 = int(sys.stdin.readline())

for i in range(n1):

    sum_ = 0
    n2 = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    max_n = numbers[-1]
    for j in numbers[::-1]:
        if max_n > j:
            sum_ += max_n-j
        elif max_n < j:
            max_n = j
    print(f'#{i+1} {sum_}')

