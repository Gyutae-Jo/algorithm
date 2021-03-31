# # 12976 - pqr
# import sys
# N_K = sys.stdin.readline().split()
# N = int(N_K[0])
# K = int(N_K[1])
# # N, K = map(int, input().split())
# # arr = list(map(int, input().split()))
# arr = sys.stdin.readline().split()

# cnt = 0
# total = 1
# for i in range(N):
#     total *= int(arr[i])
# if total % K == 0:
#     for p in range(N-2):
#         if int(arr[p]) % K == 0:
#             cnt += (N - (p+1)) * (N - (p+1) - 1) // 2
#             continue
#         for q in range(p+1, N-1):
#             if (int(arr[p]) * int(arr[q])) % K == 0:
#                 cnt += (N - (q+1))
#                 continue
#             for r in range(q+1, N):
#                 if (int(arr[p])*int(arr[q])*int(arr[r])) % K == 0:
#                     cnt += 1
#     print(cnt)
# else:
#     print(0)

N, K = map(int, input().split())
A = list(map(int, input().split()))

# K를 소인수 분해하자
K_clone = K

# 소수 구하기 (위키피디아 참조 https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]

K_dict = {}
for i in prime_list(K_clone):
    while True:
        if K_clone >= i and K_clone % i == 0:
            K_clone //= i
            K_dict[i] = K_dict.get(i, 0) + 1
        else:
            break
    if K_clone == 1:
        break
# print(prime_list(K))
# print(K_dict)

# A의 원소들은 K의 소인수들의 갯수를 세자.
A_list = []
for a in A:

    # a_dict = {i:0 for i in K_dict.keys()}
    a_list = [0 for _ in K_dict.keys()]
    # for i in a_dict.keys():
    for i in range(len(a_list)):
        while True:
            if a >= list(K_dict.keys())[i] and a % list(K_dict.keys())[i] == 0:
                a //= list(K_dict.keys())[i]
                # a_dict[i] += 1
                a_list[i] += 1
            else:
                break
    A_list.append(sum(a_list)) #######고친부분
cnt = 0
# print(A_list)
New_A = []
for i in range(N):
    New_A.append((A[i], A_list[i]))
# print(New_A)
A_New = sorted(New_A, key = lambda x : (-x[1]))
# print(A_New)
##############################
cnt = 0
total = 1
for i in range(N):
    total *= A_New[i][0]
if total % K == 0:
    for p in range(N-2):
        if A_New[p][0] % K == 0:
            cnt += (N - (p+1)) * (N - (p+1) - 1) // 2
            continue
        for q in range(p+1, N-1):
            if (A_New[p][0] * A_New[q][0]) % K == 0:
                cnt += (N - (q+1))
                continue
            for r in range(q+1, N):
                if (A_New[p][0]*A_New[q][0]*A_New[r][0]) % K == 0:
                    cnt += 1
    print(cnt)
else:
    print(0)
##############################











# A_list = sorted(A_list, key=lambda x: [-x[i] for i in range(len(A_list[0]))])

# K_list = list(K_dict.values())
# # print(K_list)

# # 만족하는지 함수 정의
# def my_func(a, b):
#     for i in range(len(a)):
#         if a[i] < b[i]:
#             return False
#     else:
#         return True

# # 리스트 합 구하기
# def list_sum(a, b):
#     temp = []
#     for i in range(len(a)):
#         temp.append(a[i] + b[i])
#     return temp

# # 중간에 만족하면 멈추는걸 해야할거같음.
# for p in range(N-2):
#     temp = A_list[p]
#     if my_func(temp, K_list):
#         cnt += (N-1-p)*(N-1-p-1)//2
#     else:
#         for q in range(p+1, N-1):
#             temp1 = list_sum(temp, A_list[q])
#             if my_func(temp1, K_list):
#                 cnt += N-1-q
#             else:
#                 for r in range(q+1, N):
#                     temp2 = list_sum(temp1, A_list[r])
#                     if my_func(temp2, K_list):
#                         cnt += 1
# print(cnt)