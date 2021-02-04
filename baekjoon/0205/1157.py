str_ = input()
result = {}
for i in str_:
    result[i.upper()] = result.get(i.upper(), 0) + 1
value_list = list(result.values())
max_value = max(value_list)
if value_list.count(max_value) == 1:
    for k, v in result.items():
        if v == max_value:
            print(k)
            break
else:
    print('?')
