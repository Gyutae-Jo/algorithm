S = input()
T = input()

# S 를 T로 만들 수 있으면 True
flag = False

while True:
    if T[-1] == 'A':
        T = T[:len(T)-1]
    elif T[-1] == 'B':
        temp = T[:len(T)-1]
        T = temp[::-1]
    if S == T:
        flag = True
        break
    if len(T) < len(S):
        break
if flag:
    print(1)
else:
    print(0)
