T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    num = list(map(int, input().split()))
    # 현재 정류장 위치
    a = 0

    # 충전 횟수
    cnt = 0
    while True:
        if a + K >= N: # 최종위치 도착하면 break
            break
        for i in range(K):
            if a+(K-i) in num: # 우선 최대 K칸 만큼 이동했을때 충전기 없으면 한칸 전으로 돌아서 충전기 있는지 확인하는것을 반복
                a = a + K - i
                cnt += 1
                break
        else: # 위의 과정에서 충전기가없어서 앞으로 전진하지 못하면 최종위치에 도착하지 못하는 것이므로 cnt = 0 선언후 break
            cnt = 0
            break
    print(f'#{tc} {cnt}')