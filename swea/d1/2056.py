n = int(input())

for i in range(n):
    ymd = input()
    print(f'#{i+1} ', end="")
    
    if (int(ymd[4:6]) in [1, 3, 5, 7, 8, 10, 12]) and (0 < int(ymd[6:]) <= 31):
        print(f'{ymd[0:4]}/{ymd[4:6]}/{ymd[6:]}')
    elif (int(ymd[4:6]) in [4, 6, 9, 11]) and (0 < int(ymd[6:]) < 31):
        print(f'{ymd[0:4]}/{ymd[4:6]}/{ymd[6:]}')
    elif int(ymd[4:6])==2 and (0 < int(ymd[6:]) <= 28):
        print(f'{ymd[0:4]}/{ymd[4:6]}/{ymd[6:]}')
    else:
        print(-1)

