'''
１. 입력받은 중위 표기식에서 토큰을 읽음
２. 토큰이 피연산자이면 토큰을 출력
３. 토큰이 연산자이면
    １. 토큰의 우선순위 > 스택의 top에 저장된 연산자 우선순위이면 스택에 push
    ２. 그렇지 않다면
        １. 스택의 top연산자 우선순위 < 토큰의 우선순위일때까지 스택에서 pop함
    ３. 스택이 비어있다면 토큰을 스택에 push
４. 토큰이 오른쪽 괄호 ) 이면
    １. 스택의 top이 ( 일때까지 스택에서 pop하여 출력
    ２. (를 출력하지는 않음
５. 중위표기식에 읽을것이 있으면 위의 내용 반복 없으면 종료
６. 스택에 남아있는 연산자를 모두 pop해서 출력

(6+5*(2-8)/2)
    6528-*2/+
'''

infix = list(input())   #입력받기
postfix = []    #출력결과 저장
stack = []      #스택
operator =["*","/","+","-"]
braket = ["(",")"]

def is_number(x):   #피연산자인지 확인
    if x not in operator and x not in braket:
        return True
    else:
        return False

def isp(token):     #isp : 스택의 top 연산자 우선순위
    if token == "*" or token =="/": return 2
    elif token=="+" or token =="-" : return 1
    elif token == "(" : return 0

def icp(token):     #icp  : 스택으로 들어갈 연산자의 우선순위
    if token == "*" or token == "/":
        return 2
    elif token == "+" or token == "-":
        return 1
    elif token == "(":
        return 3

for i in range(len(infix)):
    if is_number(infix[i]):
        postfix.append(infix[i])
    else:
        if len(stack) == 0:
            stack.append(infix[i])
        else:
            if infix[i] == ')':
                tmp = stack.pop()
                while tmp != '(':
                    postfix.append(tmp)
                    tmp = stack.pop()
            elif isp(stack[-1]) < icp(infix[i]):
                stack.append(infix[i])
            elif isp(stack[-1]) >= icp(infix[i]):
                tmp = stack.pop()
                postfix.append(tmp)
                stack.append(infix[i])
print(postfix)