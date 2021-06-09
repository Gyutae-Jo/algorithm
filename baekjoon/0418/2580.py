# # 0 카운트
# def count(i, j):
#     # 가로에서 0개수 세기(자기자신을 제외한)
#     tmp1 = 0
#     tmp1 += (arr[i].count(0) - 1)
#     # 세로에서 0개수 세기
#     tmp = 0
#     for k in range(9):
#         if arr[k][j] == 0:
#             tmp += 1
#     # cnt += (tmp - 1)
#     # 3 x 3 영역에서 0개수 세기
#     tmp2 = 0
#     if 0 <= i < 3 and 0 <= j <3:
#         for k in range(0,3):
#             tmp2 += arr[k][0:3].count(0) 
#         # cnt += (tmp2 - 1)        
#     elif 0 <= i < 3 and 3 <= j <6:
#         for k in range(0,3):
#             tmp2 += arr[k][3:6].count(0)
#         # cnt += (tmp2 - 1)
#     elif 0 <= i < 3 and 6 <= j <9:
#         for k in range(0,3):
#             tmp2 += arr[k][6:9].count(0)
#         # cnt += (tmp2 - 1)
#     elif 3 <= i < 6 and 0 <= j <3:
#         for k in range(3,6):
#             tmp2 += arr[k][0:3].count(0)
#         # cnt += (tmp2 - 1)
#     elif 3 <= i < 6 and 3 <= j <6:
#         for k in range(3,6):
#             tmp2 += arr[k][3:6].count(0)
#         # cnt += (tmp2 - 1)
#     elif 3 <= i < 6 and 6 <= j <9:
#         for k in range(3,6):
#             tmp2 += arr[k][6:9].count(0)
#         # cnt += (tmp2 - 1)
#     elif 6 <= i < 9 and 0 <= j <3:
#         for k in range(6,9):
#             tmp2 += arr[k][0:3].count(0)
#         # cnt += (tmp2 - 1)
#     elif 6 <= i < 9 and 3 <= j <6:
#         for k in range(6,9):
#             tmp2 += arr[k][3:6].count(0)
#         # cnt += (tmp2 - 1)
#     elif 6 <= i < 9 and 6 <= j <9:
#         for k in range(6,9):
#             tmp2 += arr[k][6:9].count(0)
#         # cnt += (tmp2 - 1)

#     return min(tmp, tmp1, tmp2)


# def fill(i, j):
#     if arr[i].count(0) == 1:
#         arr[i][j] = 45 - sum(arr[i])
#         return
#     else:
#         tmp = 0
#         SUM = 0
#         for k in range(9):
#             if arr[k][j] == 0:
#                 tmp += 1
#             SUM += arr[k][j]
#         if tmp == 1:
#             arr[i][j] = 45 - SUM
#             return
#         else:
#             tmp2 = 0
#             if 0 <= i < 3 and 0 <= j <3:
#                 for k in range(0,3):
#                     tmp2 += sum(arr[k][0:3])
#                 arr[i][j] = 45 - tmp2
#                 return
#             elif 0 <= i < 3 and 3 <= j <6:
#                 for k in range(0,3):
#                     tmp2 += sum(arr[k][3:6])
#                 arr[i][j] = 45 - tmp2
#                 return
#             elif 0 <= i < 3 and 6 <= j <9:
#                 for k in range(0,3):
#                     tmp2 += sum(arr[k][6:9])
#                 arr[i][j] = 45 - tmp2
#                 return
#             elif 3 <= i < 6 and 0 <= j <3:
#                 for k in range(3,6):
#                     tmp2 += sum(arr[k][0:3])
#                 arr[i][j] = 45 - tmp2
#                 return
#             elif 3 <= i < 6 and 3 <= j <6:
#                 for k in range(3,6):
#                     tmp2 += sum(arr[k][3:6])
#                 arr[i][j] = 45 - tmp2
#                 return
#             elif 3 <= i < 6 and 6 <= j <9:
#                 for k in range(3,6):
#                     tmp2 += sum(arr[k][6:9])
#                 arr[i][j] = 45 - tmp2
#                 return
#             elif 6 <= i < 9 and 0 <= j <3:
#                 for k in range(6,9):
#                     tmp2 += sum(arr[k][0:3])
#                 arr[i][j] = 45 - tmp2
#                 return
#             elif 6 <= i < 9 and 3 <= j <6:
#                 for k in range(6,9):
#                     tmp2 += sum(arr[k][3:6])
#                 arr[i][j] = 45 - tmp2
#                 return
#             elif 6 <= i < 9 and 6 <= j <9:
#                 for k in range(6,9):
#                     tmp2 += sum(arr[k][6:9])
#                 arr[i][j] = 45 - tmp2
#                 return



# arr = [list(map(int, input().split())) for _ in range(9)]
# idx = []
# for i in range(9):
#     for j in range(9):
#         if arr[i][j] == 0:
#             idx.append([i, j, count(i, j)])
# idx.sort(key=lambda x: x[2])
# for k in range(len(idx)):
#     nr = idx[k][0]
#     nc = idx[k][1]
#     fill(nr, nc)
# for i in range(9):
#     print(*arr[i])