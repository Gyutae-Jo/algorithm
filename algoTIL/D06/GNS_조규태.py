T = int(input())
for tc in range(T):
    t, N = input().split()
    num = list(input().split())
    a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    print(len(num))
    # 선택 정렬
    for i in range(len(num)-1):
        Min = i
        for j in range(i, len(num)):
            if a.index(num[j]) < a.index(num[Min]):
                Min = j
        num[i], num[Min] = num[Min], num[i]
    print(t)
    for k in range(len(num)):
        print(num[k], end=" ")
