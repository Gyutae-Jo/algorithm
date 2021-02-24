T = int(input())
for tc in range(1, T+1):
    str1 = set(input())
    str1 = list(str1)
    str2 = input()
    result = {}
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                result[str1[i]] = result.get(str1[i], 0) + 1
    Max = 0

    for key, value in result.items():
        if value > Max:
            Max = value
    print(f'#{tc} {Max}')