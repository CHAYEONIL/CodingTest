# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

Baduk = []

for i in range(19):
    Baduk.append([])
    for j in range(19):
        Baduk[i].append(0)

for i in range(19): 
    Baduk[i] = list(map(int, input().split()))

n = int(input())
for i in range(n): 
    x, y = map(int, input().split())

    for j in range(19): 
        if Baduk[x-1][j] == 0: 
            Baduk[x-1][j] = 1 
        else: 
            Baduk[x-1][j] = 0 

        if Baduk[j][y-1] == 0: 
            Baduk[j][y-1] = 1 
        else: 
            Baduk[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(Baduk[i][j], end= ' ')
    print()