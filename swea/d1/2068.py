n = int(input())

for i in range(n):
    numbers = list(map(int, input().split()))
    print(f'#{i+1} {max(numbers)}')