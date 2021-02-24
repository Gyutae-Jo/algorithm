T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    # 우선 선택정렬을 통해 num을 오름차순 정렬 한다.
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if num[min] > num[j]:
                min = j
        num[i], num[min] = num[min], num[i]

    # result는 특별한 정렬을 할 리스트이다.
    result = []
    # cnt 는 num에서 앞뒤로 하나씩 뽑아 오기 위해 필요한 숫자
    cnt = 0
    while True:
        # 짝수 인덱스에서는 큰수부터 내림차순으로 정렬되어있다.
        # 따라서 num 뒤에서 원소를 꺼내서 result에 집어넣는다.
        if cnt % 2 == 0:
            result.append(num[n-1-(cnt//2)])
            cnt += 1
            if cnt == n:
                break
        # 홀수 인덱스에서는 작은 수 부터 오름차순으로 정렬되어 있다.
        # 따라서 num 앞에서 원소를 꺼내서 result에 집어넣는다.
        else:
            result.append(num[cnt//2])
            cnt += 1
            if cnt == n:
                break

    print(f'#{tc} ', end="")
    for k in range(10):
        print(result[k], end=" ")
    print()