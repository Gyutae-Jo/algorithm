N = int(input())
arr = list(map(int,input().split()))

i = 0
flag = False # 
flag_1 = False
result = 1
cnt = 0
while True:
    if cnt == N:
        break

    if arr.count(i) == 1: # 숫자가 하나만 나온 후에 더이상 숫자 두개가 나오면 안된다.
        if flag_1 == False: # 처음 숫자 한개가 떴을 때는 
            result *= 2 # 토끼 혹은 고양이 2가지의 경우의 수가 있으므로 *2를 해준다
            flag_1 = True # 다시는 지금의 if문으로 오지않게 하기 위해
            i += 1 
            cnt += 1
        else:
            i += 1
            cnt += 1
    elif arr.count(i) == 2:
        if flag_1:
            flag = True
            break
        i += 1
        result *= 2
        cnt += 2    
    else: # 토끼, 고양이 2종류 동물밖에 없으므로 0 이하 혹은 3이상이 나올 수 없다.
        flag = True
        break

if flag:
    print(0)
else:
    print(result)