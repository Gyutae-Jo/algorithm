T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc}')
    if n // 50000:
        print(n//50000, end=' ')
        n %= 50000
    else:
        print('0',end=' ')
    if n // 10000:
        print(n//10000, end=' ')
        n %= 10000
    else:
        print('0',end=' ')
    if n // 5000:
        print(n//5000, end=' ')
        n %= 5000
    else:
        print('0',end=' ')    
    if n // 1000:
        print(n//1000, end=' ')
        n %= 1000
    else:
        print('0',end=' ')
    if n // 500:
        print(n//500, end=' ')
        n %= 500
    else:
        print('0',end=' ')
    if n // 100:
        print(n//100, end=' ')
        n %= 100
    else:
        print('0',end=' ')
    if n // 50:
        print(n//50, end=' ')
        n %= 50
    else:
        print('0',end=' ')
    if n // 10:
        print(n//10)
        n %= 10
    else:
        print('0')