N = int(input())
i = 1
while True:
    if N == 1:
        print('1/1')
        break
    if i*(i+1)/2 < N <= (i+1)*(i+2)/2:
        b = N-(i*(i+1)/2)
        if i%2==0:
            print(f'{int(i+2-b)}/{int(b)}')
            break
        else:
            print(f'{int(b)}/{int(i+2-b)}')
            break
    i += 1
    