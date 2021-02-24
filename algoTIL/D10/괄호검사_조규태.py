T = int(input())
for tc in range(1, T+1):
    string = input()
    s = []
    top = -1
    result = 1
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '{' or string[i] == '[':
            s.append(string[i])
            top += 1
        elif string[i] == ')':
            if top == -1:
                result = 0
                break
            else:
                c = s.pop()
                if c == '(':
                    top -= 1
                else:
                    result = 0
                    break
        elif string[i] == '}':
            if top == -1:
                result = 0
                break
            else:
                c = s.pop()
                if c == '{':
                    top -= 1
                else:
                    result = 0
                    break
        elif string[i] == ']':
            if top == -1:
                result = 0
                break
            else:
                c = s.pop()
                if c == '[':
                    top -= 1
                else:
                    result = 0
                    break
    if len(s):
        result = 0
    print(f'#{tc} {result}')