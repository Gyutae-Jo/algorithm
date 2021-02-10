N = int(input())
cnt_5 = 0
result = -1
if N//5 != 0 and N % 5 == 0:
    print(N//5)
else:
    while True:
        if N % 3 == 0:
            result = N//3 + cnt_5
        N -= 5
        cnt_5 += 1
        if N < 0:
            result = -1
            break
    print(result)

