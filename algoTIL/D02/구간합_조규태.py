T = int(input())
for tc in range(T):
    n_m = list(map(int, input().split()))
    n = n_m[0]
    m = n_m[1]
    Max = 0
    Min = 0
    num = list(map(int, input().split()))
    # 임의의 초기 설정
    for i in range(m):
        Max += num[i]
        Min += num[i]
        
    for i in range(len(num)-(m-1)):
        Sum = 0
        for j in range(m):
            Sum += num[i+j]
        if Sum > Max:
            Max = Sum
        if Sum < Min:
            Min = Sum
    print(f'#{tc+1} {Max-Min}')