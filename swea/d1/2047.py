str_ = input()

for i in str_:
    if i.isalpha():
        print(i.upper(), end="")
    else:
        print(i, end="")