T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    i = 0
    result = 0
    for _ in range(len(str2)-len(str1)+1):
        cnt = 0
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                i += 1
                cnt += 1
                if cnt == len(str1):
                    result = 1
                    break
            else:
                i -= (j-1)
                break

        if cnt == len(str1):
            break

    print(f'#{tc} {result}')