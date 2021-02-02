n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        print(f'#{i+1} >')
    elif a < b:
        print(f'#{i+1} <')
    else:
        print(f'#{i+1} =')