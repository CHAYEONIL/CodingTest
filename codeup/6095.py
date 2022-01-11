# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

Baduk = []
for i in range(20):
    Baduk.append([])
    for j in range(20):
        Baduk[i].append(0)

n = int(input())

for i in range(n):
    x,y = map(int, input().split())
    Baduk[x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(Baduk[i][j], end = ' ')
    
    print()