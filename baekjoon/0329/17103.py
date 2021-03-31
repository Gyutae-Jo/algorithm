# 17103 - 골드바흐 파티션


N = 1000000


check = [False,False] + [True]*(N-1)
primes = []

for i in range(2, N+1):
    if check[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            if check[j]:
                check[j] = False

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    n = int(input())
    for x in primes:
        if (x <= (n-x)) and check[n-x]:
            cnt += 1
    print(cnt)  


