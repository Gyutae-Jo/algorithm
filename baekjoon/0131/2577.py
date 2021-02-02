import sys
n=1
for i in range(3):
    n *= int(sys.stdin.readline())

result = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0
}

while n != 0:
    result[n%10] += 1
    n = n//10

for i in result:
    print(result[i])
