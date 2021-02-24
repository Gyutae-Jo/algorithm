'''
1,2,3,4,5,6,7,8,9,10의 powerset 중 원소의 합이 10인 부분집합을 구하시오
'''

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subset = [0] * 10

def powerset(idx):
    if idx == 10:
        Sum = 0
        tmp = []
        for i in range(len(subset)):
            if subset[i]:
                Sum += arr[i]
                tmp.append(arr[i])
        if Sum == 10:
            print(tmp)
            return tmp
        return
    subset[idx] = 0
    powerset(idx+1)

    subset[idx] = 1
    powerset(idx+1)

powerset(0)