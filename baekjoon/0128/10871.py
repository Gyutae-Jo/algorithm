import sys # 

N_X=sys.stdin.readline().split() # split()으로 무조건 리스트로 담고 생각하자. rstrip()으로 str으로 인풋받으면 마지막 숫자가 몇자리인지 알기 귀찮기 때문에
A = sys.stdin.readline().split() 

for i in A:
    if int(N_X[-1]) > int(i): 
        print(int(i), end=" ")


# # N, X = map(int, input().split())
# # A = list(map(int, input().split()))

# # for i in A:
# #     if X > i:
# #         print(i, end=" ")
