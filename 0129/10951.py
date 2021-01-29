import sys
while True:
    try:
        n = sys.stdin.readline().split()
        print(int(n[0])+int(n[1]))
    except:
        break
    