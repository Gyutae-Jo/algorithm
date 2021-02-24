for i in range(10):
    n = int(input())
    # 100x100 2차원 배열을 입력 받는다.
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 첫 행을 다 더한 값을 구해서 초기 결과값으로 설정한다
    result = 0
    for j in range(100):
        result += arr[0][j]

    # 대각선 합은 for 문 한번만 돌면 되서 밖에다가 초기화
    temp_cross1 = 0
    temp_cross2 = 0
    for x in range(100):
        temp_row = 0
        temp_col = 0
        for y in range(100):
            temp_row += arr[x][y]
            temp_col += arr[y][x]
        # 각 행 더한 값과 각 열 더한 값을 결과값과 비교해서 더 크면 결과값이 더 큰값으로 교체된다.
        if temp_row > result:
            result = temp_row
        if temp_col > result:
            result = temp_col

        temp_cross1 += arr[x][x]
        temp_cross2 += arr[99-x][x]

    # 대각선 합도 마찬가지로 결과값보다 크면 교체한다.
    if temp_cross1 > result:
        result = temp_cross1
    if temp_cross2 > result:
        result = temp_cross2

    print(f'#{n} {result}')
