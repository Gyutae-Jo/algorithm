T = int(input())
for tc in range(T):
    P, A, B = map(int, input().split())
    cnt_A = 0
    cnt_B = 0
    l_A = 1
    l_B = 1
    r_A = P
    r_B = P
    # while 한번 써서 먼저 탐색을 끝낸 쪽이 이긴다.
    while True:
        # 만약에 동시에 탐색이 끝나면 비긴다.
        if int((l_A+r_A)/2) == A and int((l_B+r_B)/2) == B:
            print(f'#{tc+1} 0')
            break
        # 위에서 동시에 끝나는 경우가 제거되서 둘 중 한명이 이길때를 판별
        elif int((l_A+r_A)/2) == A or int((l_B+r_B)/2) == B:
            if int((l_A+r_A)/2) == A:
                print(f'#{tc + 1} A')
                break
            else:
                print(f'#{tc + 1} B')
                break
            break
        # 탐색이 끝나지 않는 경우 시작점과 끝점을 설정해준다.
        if int((l_A+r_A)/2) > A:
            r_A = int((l_A+r_A)/2)
            cnt_A += 1
        elif int((l_A+r_A)/2) < A:
            l_A = int((l_A+r_A)/2)
            cnt_A += 1

        if int((l_B+r_B)/2) > B:
            r_B = int((l_B+r_B)/2)
            cnt_A += 1
        elif int((l_B+r_B)/2) < B:
            l_B = int((l_B+r_B)/2)
            cnt_A += 1
