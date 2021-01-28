import sys

n =  int(sys.stdin.readline())

for i in range(n):
    A_B = sys.stdin.readline().rstrip()
    A = int(A_B[0])
    B = int(A_B[-1])
    print(f'Case #{i+1}: {A} + {B} = {A+B}')