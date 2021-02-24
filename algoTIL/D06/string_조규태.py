# 숫자를 string으로 변환
def itoa(num):
    N = num
    result = ""
    while N != 0:
        result = f'{N%10}' + result
        N //= 10
    return result


# reverse 3가지 방법
a = "abcd"
b = ""
for i in range(len(a)):
    b = a[i] + b
print(b)

#
a = "abcd"
b = a[::-1]
print(b)

#
a = "abcd"
b = list(a)

for i in range(len(b)//2):
    b[i], b[len(b)-1-i] = b[len(b)-1-i], b[i]
c = "".join(b)
print(c)