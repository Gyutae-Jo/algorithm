import sys
n = sys.stdin.readline().split()
while not(n[0] == '0' and n[1] == '0'):
    print(int(n[0])+int(n[1]))
    n = sys.stdin.readline().split()