T = int(input())
for tc in range(T):
    n = int(input())
    N = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        tmp[2] += 1
        tmp[3] += 1
        N.append(tmp)
    area = 0
    for i in range(n-1):
        for j in range(i+1, n):
            # 다른 색인지 확인
            if N[i][-1] != N[j][-1]:
                # 안겹치는 경우는 pass
                if N[i][2] <= N[j][0] or N[i][0] >= N[j][2] or N[i][3] <= N[j][1] or N[j][3] <= N[i][1]:
                    pass
                # 겹치는 경우
                else:
                    # 겹치는 경우에는 x값 4개를 정렬하면 가운데 2개가 겹치는 상자의 모서리값이다.
                    # y도 마찬가지
                    x = [N[i][0], N[i][2], N[j][0], N[j][2]]
                    y = [N[i][1], N[i][3], N[j][1], N[j][3]]
                    # 선택 정렬
                    for k in range(0, len(x)-1):
                        min_x = k
                        min_y = k
                        for l in range(k+1, len(x)):
                            if x[l] < x[min_x]:
                                min_x = l
                            if y[l] < y[min_y]:
                                min_y = l
                        x[min_x], x[k] = x[k], x[min_x]
                        y[min_y], y[k] = y[k], y[min_y]
                    area += (x[2]-x[1])*(y[2]-y[1])
    print(f'#{tc+1} {area}')