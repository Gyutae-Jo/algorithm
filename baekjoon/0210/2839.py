N = int(input())

if N % 5 == 0:
    print(N//5)
else:
    if (N%5)%3 == 0:
        print(N//5 + (N%5)//3)
    else:
        r = N % 5
        i = 1
        while r <= N:
            if r % 3 == 0:
                print(N//5 - (i-1) + r // 3)
                break
            r += 5
            i += 1
        if r > N:
            print(-1)

