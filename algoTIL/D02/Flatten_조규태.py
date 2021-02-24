for tc in range(1, 11):
    N = int(input())
    num = list(map(int, input().split()))
    # 최대값과 최소값을 가지질 때의 인덱스
    Max_idx = 0
    Min_idx = 0
    for i in range(N):
        for j in range(len(num)):
            if num[j] > num[Max_idx]: # 최대값 찾기
                Max_idx = j # 최대값일때의 인덱스
        for k in range(len(num)):
            if num[k] < num[Min_idx]: # 최소값 찾기
                Min_idx = k # 최소값일때의 인덱스
        if num[Max_idx] - num[Min_idx] <= 1: # 덤프 횟수가 N번 반복되기 전에 이미 고르게 됐는지를 판단해서 break
            break
        num[Max_idx] -= 1
        num[Min_idx] += 1
    # N번 덤프 행위가 끝났으므로 마지막으로 최대값과 최소값구한 다음 출력
    for j in range(len(num)):
        if num[j] > num[Max_idx]:
            Max_idx = j
    for k in range(len(num)):
        if num[k] < num[Min_idx]:
            Min_idx = k
    print(f'#{tc} {num[Max_idx]-num[Min_idx]}')