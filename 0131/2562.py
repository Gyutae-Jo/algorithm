import sys
result = []
for i in range(9):
    result.append(int(input()))

for i in enumerate(result):
    if i[1] == max(result):
        print(max(result))
        print(i[0]+1)
