for tc in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
    if (x2>p1) or (q1<y2) or (y1>q2) or (x1>p2):
        print('d')
    elif x2==p1:
        if y1==q2 or y2==q1:
            print('c')
        else:
            print('b')
    elif x1==p2:
        if y1==q2 or y2==q1:
            print('c')
        else:
            print('b')
    elif y1==q2:
        if x2==p1 or x1==p2:
            print('c')
        else:
            print('b')
    elif q1==y2:
        if x2==p1 or x1==p2:
            print('c')
        else:
            print('b')
    else:
        print('a')