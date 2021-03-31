
N = int(input())
start = 1
end = N

while True:
    if ((start+end)//2)**2 == N:
        print((start+end) // 2)
        break
    elif ((start+end)//2)**2 < N:
        start = (start+end)//2 + 1
    elif ((start+end)//2)**2 > N:
        end = (start+end)//2 - 1