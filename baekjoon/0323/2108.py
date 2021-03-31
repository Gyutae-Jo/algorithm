import sys
n = int(sys.stdin.readline())
list_n = []
for i in range(n):
    a = int(sys.stdin.readline())
    list_n.append(a)

print(round(sum(list_n)/len(list_n)))
print(sorted(list_n)[len(list_n)//2])
if n == 1:
    print(list_n[0])
else:
    dict_n = {}
    for i in list_n:
        dict_n[i] = dict_n.get(i, 0) + 1
    tmp = list(dict_n.items())
    tmp.sort(key=lambda x : (x[1], x[0]))
    max_cnt = tmp[-1][1]
    tmp_cnt = 0
    for i in tmp:
        if i[1] == max_cnt:
            tmp_cnt += 1
    if tmp_cnt == n:
        print(tmp[1][0])
    else:
        tmp2 = []
        for i in tmp:
            if i[1] == max_cnt:
                tmp2.append(i)
        if len(tmp2) == 1:
            print(tmp2[0][0])
        else:
            print(tmp2[1][0])
    
print(max(list_n)-min(list_n))