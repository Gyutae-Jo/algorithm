T = int(input())
for tc in range(T):
    n = int(input())
    num = input()
    cnt = [0]*10
    for i in num:
        cnt[int(i)] += 1
    max_cnt = cnt[0]
    max_num = 0
    for i in range(len(cnt)):
        if max_cnt <= cnt[i]:
            max_cnt = cnt[i]
            max_num = i
    print(f'#{tc+1} {max_num} {max_cnt}')
