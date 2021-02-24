T = int(input())
for tc in range(1, T+1):
    string = input()

    while True:
        s = [""] * len(string)
        top = -1
        top += 1
        s[top] = string[0]
        for i in range(1, len(string)):
            if string[i] == s[top]:
                s[top] = ""
                top -= 1
            else:
                top += 1
                s[top] = string[i]
        string2 = "".join(s)
        if string == string2:
            break
        else:
            string = string2
    print(f'#{tc} {len(string)}')
