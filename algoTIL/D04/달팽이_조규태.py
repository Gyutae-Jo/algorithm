T = int(input())
# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    i = 0 # 행
    j = 0 # 열
    # 우하좌상을 선택할 기준될 값이다.
    # k%4 -> 0이면 우, 1이면 하, 2이면 좌, 3이면 상
    k = 0

    v = 1 # 행렬 값
    while True:
        if k % 4 == 0: # 우
            arr[i][j] = v
            if v == n**2: # 행렬값이 마지막 숫자이면 멈춤
                break
            v += 1
            # 우로 가면서 인덱스를 벗어나거나 이미 행렬값이 있을 때는 하로 간다.
            if j+dc[k%4] > n-1 or arr[i][j+dc[k%4]] != 0:
                k += 1
                i += dr[k % 4]
                j += dc[k % 4]
            else: # 그게 아니면 우로 진행
                i += dr[k % 4]
                j += dc[k % 4]

        elif k % 4 == 1: # 하
            arr[i][j] = v
            if v == n**2:
                break
            v += 1
            if i+dr[k%4] > n-1 or arr[i+dr[k%4]][j] != 0:
                k += 1
                i += dr[k % 4]
                j += dc[k % 4]
            else:
                i += dr[k % 4]
                j += dc[k % 4]

        elif k % 4 == 2:
            arr[i][j] = v
            if v == n**2:
                break
            v += 1
            if j+dc[k%4] < 0 or arr[i][j+dc[k%4]] != 0:
                k += 1
                i += dr[k % 4]
                j += dc[k % 4]
            else:
                i += dr[k % 4]
                j += dc[k % 4]

        elif k % 4 == 3:
            arr[i][j] = v
            if v == n**2:
                break
            v += 1
            # 상으로 이동할때는 인덱스를벗어나기전에
            # 이미 정의된 값을 먼저 만난다.
            if arr[i+dr[k%4]][j] != 0:
                k += 1
                i += dr[k % 4]
                j += dc[k % 4]
            else:
                i += dr[k % 4]
                j += dc[k % 4]
    print(f'#{tc}')
    for a in range(n):
        for b in range(n):
            print(arr[a][b], end=" ")
        print()


# 카운팅정렬 연습
# a = [2,5,4,1,3] # 입력배열
# b = [0]*len(a)
# Max = max(a)
# cnt = [0] * (Max+1) # 카운트 배열
# for i in a:
#     cnt[i] += 1
# for j in range(Max):
#     cnt[j+1] += cnt[j]
#
# for k in range(len(a)-1,-1,-1):
#     b[cnt[a[k]]-1] = a[k]
#     cnt[a[k]] -= 1
# print(b)
# # 선택정렬
# a = [3,3,1,2]
# for i in range(0, len(a)-1):
#     min = i
#     for j in range(i+1, len(a)):
#         if a[min] > a[j]:
#             min = j
#     a[i], a[min] = a[min], a[i]