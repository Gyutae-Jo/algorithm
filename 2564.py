x, y = map(int, input().split())
n = int(input())
store = []
for i in range(n):
    a, b = map(int, input().split())
    store.append(a)
    store.append(b)
result = 0
# 동근이 위치
a, b = map(int, input().split())
for i in range(n):
    if a == store[i*2]:
        result += abs(store[i*2+1]-b)
    elif a == 1:
        if store[i*2] == 2:
            if store[i*2+1] + b < (2*x - (store[i*2+1]+b)):
                result = result + store[i*2+1] + b + y
            else:
                result = result + 2*x - (store[i*2+1]+b) + y
        elif store[i*2] == 3:
            result += (store[i*2+1]+b)
        elif store[i*2] == 4:
            result += ((x-b)+store[i*2+1])
    elif a == 2:
        if store[i*2] == 1:
            if store[i*2+1] + b < (2*x - (store[i*2+1]+b)):
                result = result + store[i*2+1] + b + y
            else:
                result = result + 2*x - (store[i*2+1]+b) + y
        elif store[i*2] == 3:
            result += (y-store[i*2+1]+b)
        elif store[i*2] == 4:
            result += (x+y-store[i*2+1]-b)
    elif a == 3:
        if store[i*2] == 1:
            result = result + store[i*2+1] + b
        elif store[i*2] == 2:
            result += (store[i*2+1]+y-b)
        elif store[i*2] == 4:
            if store[i*2+1] + b < (2*y - (store[i*2+1]+b)):
                result = result + store[i*2+1] + b + x
            else:
                result = result + 2*y - (store[i*2+1]+b) + x
    elif a == 4:
        if store[i*2] == 1:
            result += (x-store[i*2+1]+b)
        elif store[i*2] == 2:
            result += (x+y-store[i*2+1]-b)
        elif store[i*2] == 3:
            if store[i*2+1] + b < (2*y - (store[i*2+1]+b)):
                result = result + store[i*2+1] + b + x
            else:
                result = result + 2*y - (store[i*2+1]+b) + x
print(result)