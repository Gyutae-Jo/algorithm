T = int(input())
for tc in range(1, T+1):
    stick = input()

    cnt = 0
    ans = 0
    for i in range(len(stick)):
        if stick[i] == "(":
            cnt += 1
        else:
            cnt -= 1
            if stick[i-1] == "(":
                ans += cnt
            else:
                ans += 1
    print(f'#{tc} {ans}')
