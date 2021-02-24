T = int(input())
for tc in range(T):
    n = int(input())
    num = list(map(int, input().split()))
    # 임의의 초기 설정
    Max = num[0]
    Min = num[0]
    for i in num:
        if Max < i:
            Max = i
        if Min > i:
            Min = i
    print(f'#{tc+1} {Max-Min}')