a= int(input())
b= int(input())
result = 0
i = 1
while b != 0:
    print(a*(b%10)) 
    result = result + a*(b%10) * i
    b //= 10
    i *= 10
print(result)