n = int(input())
i = 1
while True:
    if n==1:
        print(1)
        break
    if (3*(i**2)-3*i+1) < n <= (3*((i+1)**2)-3*(i+1)+1):
        print(i+1)
        break
    i += 2