for tc in range(10):
    T = int(input())
    Str = [list(input()) for _ in range(100)]
    tmp_r = ""
    tmp_c = ""
    Max = 1 # 회문 최대 길이
    for k in range(2, 101): # k는 회문 길이
        for i in range(100):
            for j in range(101-k):
                tmp_r = ""
                tmp_c = ""
                for l in range(j, j+k):
                    tmp_r += Str[i][l]
                    tmp_c += Str[l][i]
                if tmp_r == tmp_r[::-1] or tmp_c == tmp_c[::-1]:
                    Max = k
                    break
            if tmp_r == tmp_r[::-1] or tmp_c == tmp_c[::-1]:
                break
    print(f'#{tc+1} {Max}')