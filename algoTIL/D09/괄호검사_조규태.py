T = int(input())
for tc in range(1, T+1):
    Input = input()
    s = list()
    top = -1
    result = True
    for i in range(len(Input)):
        if Input[i] == '(':
            s.append(Input[i])
            top += 1
        else:
            if top == -1:
                result = False
                break
            elif s[top] == '(':
                s.pop()
                top -= 1 # top에 원소 삭제
    if len(s) != 0:
        result = False
    print(f'#{tc} {result}')

