n = int(input())

for i in range(n):
    numbers = list(map(int, input().split()))
    avg = int(round(sum(numbers)/len(numbers), 0))
    print(f'#{i+1} {avg}')