n = int(input())

for i in range(n):
    numbers = list(map(int, input().split()))
    sum_ = 0
    for j in numbers:
        if j % 2:
            sum_ +=j
    print(f'#{i+1} {sum_}')