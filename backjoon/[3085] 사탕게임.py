n = int(input())

array = []

for _ in range(n) :
    colors = list(map(str, input()))
    array.append(colors)

maxCount = 0 # 사탕 최대 개수

# 배열의 행 같은 색 계산
def width():
    global maxCount

    for k in range(n):
        countRow = 1 # 초기 개수 1
        for l in range(n - 1):
            if array[k][l] == array[k][l + 1]:
                countRow += 1
                maxCount = max(maxCount, countRow) #증가시킨 값과 최대 사탕개수를 비교하여 큰값 대입
            else:
                countRow = 1

# 배열의 열 같은 색 계산
def height():
    global maxCount

    for k in range(n):
        countcolumn = 1 # 초기 개수 1
        for l in range(n - 1):
            if array[l][k] == array[l - 1][k]:
                countcolumn += 1
                maxCount = max(maxCount, countcolumn) #증가시킨 값과 최대 사탕개수를 비교하여 큰값 대입
            else:
                countcolumn = 1

for i in range(n):
    for j in range(n-1):
        # 만약 입력 받은 배열의 행의 원소가 다르다면
        if array[i][j] != array[i][j+1]:
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
            width()
            height()
            array[i][j + 1], array[i][j] = array[i][j], array[i][j + 1]
        # 만약 입력 받은 배열의 열의 원소가 다르다면
        if array[j][i] != array[j + 1][i]:
            array[j][i], array[j + 1][i] = array[j + 1][i], array[j][i]
            width()
            height()
            array[j + 1][i], array[j][i] = array[j][i], array[j + 1][i]

print(maxCount)