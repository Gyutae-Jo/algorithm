T = int(input())
for tc in range(1, T+1):
    # input 받은 str이 들어잇음
    arr = [input() for _ in range(5)]
    # str중에 가장 긴 문자열의 길이 찾기
    Max_len = 0
    for i in range(len(arr)):
        if len(arr[i]) > Max_len:
            Max_len = len(arr[i])

    # 가장 긴 문자열을 기준으로 모두 "" 빈공백을 원소로 같는 배열 생성
    arr2 = [["" for _ in range(Max_len)] for _ in range(5)]

    # 인풋받은 문자열을 arr2에 대입
    for i in range(5):
        for j in range(len(arr[i])):
            arr2[i][j] = arr[i][j]
    # 출력
    print(f'#{tc} ', end="")
    for j in range(len(arr2[0])):
        for i in range(len(arr2)):
            print(arr2[i][j], end="")
    print()
