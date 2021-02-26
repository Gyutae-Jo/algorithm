N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
patch1 = "WBWBWBWB"
patch2 = "BWBWBWBW"
Min = 64
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt_1 = 0
        cnt_2 = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if arr[i+k][j+l] != patch1[l]:
                        cnt_1 += 1
                    if arr[i+k][j+l] != patch2[l]:
                        cnt_2 += 1
                elif k % 2 == 1:
                    if arr[i+k][j+l] != patch2[l]:
                        cnt_1 += 1
                    if arr[i+k][j+l] != patch1[l]:
                        cnt_2 += 1
        if Min > cnt_1:
            Min = cnt_1
        if Min > cnt_2:
            Min = cnt_2
print(Min)