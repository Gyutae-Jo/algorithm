def six3(N):
    n = str(N)
    cnt = 0
    for i in range(len(n)-3+1):
        if n[i] == '6' and n[i+1] == '6' and n[i+2] == '6':
            return True
    return False




n = int(input())
cnt = 0
i = 666
while cnt != n:
    if six3(i):
        cnt += 1
    i += 1
print(i-1)
    