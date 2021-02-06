s = input()
cnt = 0
for i in s:
    if (ord(i)+1)//3 == 22:
        cnt += 3
    elif (ord(i)+1)//3 == 23:
        cnt += 4
    elif (ord(i)+1)//3 == 24:
        cnt += 5
    elif (ord(i)+1)//3 == 25:
        cnt += 6
    elif (ord(i)+1)//3 == 26:
        cnt += 7
    elif ord(i)//4 == 20:
        cnt += 8
    elif ord(i)//3 == 28:
        cnt += 9
    else:
        cnt += 10
print(cnt)
