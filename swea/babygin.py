def check(arr):
    # triple
    for i in range(10):
        if arr[i] == 3:
            return True
    for j in range(8):
        if arr[j] and arr[j+1] and arr[j+2]:
            return True
    return False
T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    result = 0
    for i in range(len(num)):
        if i % 2 == 0:
            p1[num[i]] += 1
            if check(p1):
                result = 1
                break
        else:
            p2[num[i]] += 1
            if check(p2):
                result = 2
                break
    print(f'#{tc} {result}')