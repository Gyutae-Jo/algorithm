T = int(input())
for tc in range(1, T+1):
    N_M_K = list(map(int, input().split()))
    N = N_M_K[0] # N명
    M = N_M_K[1] # M초
    K = N_M_K[2] # K개
    S = list(map(int, input().split())) # 사람들 방문 시간(초)가 들어있음
    last_S = S[0] # 마지막에 방문하는 사람의 시간(초)
    for i in S:
        if i > last_S:
            last_S = i
    result = [0]*(last_S+1) # 붕어빵 재고가 몇초에 몇개 있는지
    for i in range(len(result)):
        result[i] = (i//M)*K # 2명 2초 2개 -> [0,0,2,2,4]
    # print(result)
    for i in S:
        for j in range(len(result)-i):
            result[i+j] -= 1
    # print(result)
    for i in result:
        if i < 0:
            print(f'#{tc} Imopossible')
            break
    else:
        print(f'#{tc} possible')
