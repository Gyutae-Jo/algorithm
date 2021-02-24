T = int(input())
for tc in range(T):
    # N 개의 버스 노선
    N = int(input())
    # bus_station에는 앞에서 부터 2개씩 A정류장, B정류장 숫자가 들어간다
    bus_station = []
    for i in range(N):
        A, B = map(int, input().split())
        bus_station.append(A)
        bus_station.append(B)
    # 정류장 번호 중에서 가장 큰값을 구한다.
    Max_bus_station = 0
    for i in bus_station:
        if Max_bus_station < i:
            Max_bus_station = i
    # BUS 는 각 (인덱스+1) 정류장에 지나가는 버스의 수가 들어가게 된다.
    # BUS = [0] * Max_bus_station
    BUS = [0] *5001
    for i in range(0,len(bus_station),2): # A, B 번호가 반복되므로 2씩 for문을 돌린다.
        A = bus_station[i]
        B = bus_station[i+1]
        for j in range(A,B+1):
            BUS[j-1] += 1 # A이상 B이하 정류장에 버스가 지나가므로 +1
    P = int(input())
    result = ""
    for i in range(P):
        C = int(input())
        result = result + " " +str(BUS[C-1])
    print(f'#{tc + 1}'+result)
