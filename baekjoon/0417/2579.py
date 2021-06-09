n = int(input())
stair = [0] * n

for i in range(n):
    s = int(input())
    stair[i] = s
# stair = stair[::-1]
max_score = [0] * n

if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0]+stair[1])
elif n == 3:
    a1 = stair[0] + stair[2]
    a2 = stair[1] + stair[2]
    print(max(a1, a2))
else:
    max_score[0] = stair[0]
    max_score[1] = stair[0] + stair[1]
    # flag = True
    # if stair[0] + stair[1] > stair[0] + stair[2]:
    #     max_score[2] = max_score[1]
    #     flag = False
    # else:
    #     max_score[1] -= stair[1]
    #     max_score[2] = stair[0] + stair[2]
    #     flag = False
    a1 = stair[0] + stair[2]
    a2 = stair[1] + stair[2]
    max_score[2] = max(a1, a2)
    for i in range(3, n):
        # 전 칸에서 올라온 경우 + 전전 칸에서 올라온 경우
        max_score[i] = max(max_score[i-3] + stair[i-1] + stair[i], max_score[i-2] + stair[i])




        # # 이전에 연속으로 두칸 간 경우
        # if flag:
        #     # 이전 계단을 밟는것보다 현재 계단을 밟는게 더 이득인 경우
        #     if stair[i] + max_score[i-2] > max_score[i-1]:
        #         max_score[i-1] -= stair[i-1]
        #         max_score[i] = stair[i] + max_score[i-2]
        #         flag = False
        #     # 현재 계단을 안밟는게 더 이득인 경우
        #     else:
        #         max_score[i] = max_score[i-1]
        #         flag = False
        # # 이전에 연속으로 두칸을 밟지 않았을 경우 0칸 혹은 1칸을 밟은 경우
        # else:
        #     max_score[i] = stair[i] + max_score[i-1]
        #     # i-1번째 계단을 밟았을 경우 i번째 계단을 밟으면 연속 2계단 밟은 것이므로 flag = True 
        #     if max_score[i-1] != max_score[i-2]:
        #         flag = True
    print(max_score[-1])