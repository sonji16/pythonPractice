size = 100
arr_ma = []

for i in range(size):
    arr_ma.append([0] * size)

# 첫 시작 위치는 고정
x = int(size / 2)
y = size - 1

# 첫 숫자 1은 고정 위치에 저장
arr_ma[y][x] = 1

# 숫자 2부터 저장을 시작합니다
for i in range(2, (size * size) + 1):
    # 일단 둘 다 증가시킨 뒤 판단 시작
    x = x + 1
    y = y + 1

    print("y : {0} x : {1}". format(y, x))

    # 1 둘다 벗어났다면 이전 숫자 위치 위쪽 칸에 채움
    if x >= size and y >= size:
        x = x - 1
        y = y - 2
    elif x >= size: # x만 벗어 났다면 현재 위치에서 x만 처음 위치로
        x = 0
    elif y >= size: # y만 벗어 났다면 현재 위치에서 y만 처음 위치로
        y = 0
    else: # 둘다 벗어나지 않았고 해당 위치에 값이 비어있지 않다면 이전 위치 위로
        if arr_ma[y][x] > 0:
            x = x - 1
            y = y - 2

    arr_ma[y][x] = i # 값 넣기

    for col in range(size):
        print(arr_ma[col])

# 검증 행
for col in range(size):
    sum = 0
    for row in range(size):
        sum = sum + arr_ma[col][row]

    print("col:{0} sum: {1}".format(row, sum))

# 검증 대각선
sum = 0
for i in range(size):
    sum = sum + arr_ma[i][i]

print("대각선 sum: {0}".format(sum))