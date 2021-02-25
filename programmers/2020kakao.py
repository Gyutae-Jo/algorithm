def rev(u):
    u = u[1:]
    u = u[:-1]
    result = ""
    for i in u:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result

def div(w):
    stack_open = []
    stack_close = []
    index = 0
    for i in range(len(w)):
        if w[i] == '(':
            stack_open.append(w[i])
        else:
            stack_close.append(w[i])
        if len(stack_open) == len(stack_close):
            index = i
            break
    return w[:i+1], w[i+1:]
    
def cor(u):
    if u[0] == '(':
        return True
    return False

def solution(p):
    if len(p) == 0:
        return ""
    # p --> u,v 나누기
    u = div(p)[0]
    v = div(p)[1]
    if cor(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + rev(u)