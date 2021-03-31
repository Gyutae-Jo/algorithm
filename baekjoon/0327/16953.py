A, B = map(int, input().split())


cnt = 0
# -1 을 출력해야되는 경우에 True 값을 가진다.
flag = False 
while True:
    if A == B:
        break
    elif A > B:
        flag = True
        break
    if B % 2: # 홀수 일때
        if B % 10 == 1:
            cnt += 1
            B //= 10
        else:
            flag = True
            break   
    else: # 짝수 일때
        cnt += 1
        B //= 2 

if flag:
    print(-1)
else:
    print(cnt+1)
