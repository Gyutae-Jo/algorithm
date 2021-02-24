data = [-7, -3, -2, 5, 8]

result = False
for i in range(1, 1<<len(data)):
    Sum = 0
    for j in range(len(data)):
        if i & (1<<j):
            Sum += data[j]
    if Sum == 0:
        result = True
print(result)
