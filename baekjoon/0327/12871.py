s = input()
t = input()

# f(s) == f(t) 이면 True
flag = True

if len(s) == len(t):
    if s != t:
        flag = False
elif len(s) != len(t):
    if s * len(t) != t * len(s):
        flag = False


if flag:
    print(1)
else:
    print(0)