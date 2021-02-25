T = int(input())
for tc in range(1, T+1):
    S, E = map(int, input().split())

    Length = E - S

    i = 1
    while i*(i+1) <= Length/2:
        i += 1
    print()