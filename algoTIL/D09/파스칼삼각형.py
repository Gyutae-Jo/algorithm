def pascal(i,j):
    if i==0 and j==0:
        return 1
    elif i==0 and j!=0:
        return 0
    elif j==0 and i!=0:
        return 1
    return pascal(i-1,j-1)+pascal(i-1,j)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(pascal(i, j), end=" ")
        print()