T = int(input())
for tc in range(T):
    H,W,N = map(int, input().split())
    if N%H == 0:
        if (N//H)//10 == 0: 
            print(f'{H}0{N//H}')
        else:
            print(f'{H}{N//H}')
    else:
        if (N//H+1)//10 == 0: 
            print(f'{N%H}0{N//H+1}')
        else:
            print(f'{N%H}{N//H+1}')