import sys
# def people(k,n):
#     if n==1:
#         return 1
#     if k==0:
#         return n
#     return people(k-1, n) + people(k, n-1)
# T = int(sys.stdin.readline())
# for tc in range(T):
#     k1 = int(sys.stdin.readline())
#     n1 = int(sys.stdin.readline())
#     print(people(k1,n1)) 
# 재귀함수로 풀면 시간초과 뜸
T = int(sys.stdin.readline())
for tc in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    people = [i for i in range(1, n+1)]
    for _ in range(k):
        for i in range(1, n):
            people[i] = people[i] + people[i-1]
    print(people[-1])