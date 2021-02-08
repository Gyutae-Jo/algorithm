T = int(input())
result = 0
for tc in range(T):
    cnt = 0
    num = input()
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            cnt += 1
    if cnt + 1 == len(set(num)):
        result += 1
print(result)

