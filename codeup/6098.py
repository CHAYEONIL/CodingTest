# 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.
# 성실한 개미가 이동한 경로를 9로 표시해 출력한다.

m = []

for i in range(10):
    m.append([])
    for j in range(10):
        m[i].append(0)

for i in range(10): 
    m[i] = list(map(int, input().split()))

# for i in range(10): 
# m.append(list(map(int, input().split())))
x, y = 1, 1

while True:
    if m[x][y] == 0:
        m[x][y] = 9
    elif m[x][y] == 2:
        m[x][y] = 9
        break

    if (m[x][y+1] == 1 and m[x+1][y] == 1):
        break

    if m[x][y+1] != 1:
        y = y + 1
    elif m[x+1][y] != 1:
        x = x + 1

# print()

for i in range(10):
    for j in range(10):
        print(m[i][j], end = ' ')
    print()