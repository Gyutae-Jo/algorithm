for tc in range(4):
    num = list(map(int, input().split()))
    if num[2] < num[4] or num[0] > num[6] or num[1] > num[7] or num[3] < num[5]:
        print('d')
    elif num[1] == num[7] and num[2] == num[4]:
        print('c')
    elif num[3] == num[5] and num[2] == num[4]:
        print('c')
    elif num[0] == num[6] and num[3] == num[1]:
        print('c')
    elif num[0] == num[6] and num[1] == num[7]:
        print('c')
    elif num[0] < num[4] < num[2] and num[1]<num[5]<num[3]:
        print('a')
    elif num[0] < num[6] < num[2] and num[1]<num[7]<num[3]:
        print('a')
    elif num[0] < num[4] < num[2] and num[1]<num[7]<num[3]:
        print('a')
    elif num[0] < num[6] < num[2] and num[1]<num[5]<num[3]:
        print('a')
    elif num[0] <num[4] and num[6] <num[2] and num[5] < num[1] and num[7] > num[3]:
        print('a')
    else:
        print('b')
