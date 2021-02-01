def self_n(n):
    new_n = n
    while n != 0:
        new_n += (n%10)
        n //= 10
    return new_n
result = list(range(1,10001))
for i in range(1, 10001):
    if self_n(i) > 10000:
        pass
    result[self_n(i)-1] = 0

for i in result:
    if i != 0:
        print(i)

