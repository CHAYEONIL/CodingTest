T = int(input())
delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]

    mid = N >> 1
    matrix[mid][mid] = 2
    matrix[mid-1][mid-1] = 2
    matrix[mid-1][mid] = 1
    matrix[mid][mid-1] = 1

    for i in range(M):
        x, y, c = map(int, input().split())
        # 각각 보드위의 행, 열, 색을 저장한다.
        y, x = y-1, x-1

        for i in range(8):
            dx, dy = delta[i]
            nx, ny = x + dx, y + dy
            while True:
                if nx < 0 or ny < 0 or nx > N-1 or ny > N-1: # 모서리인가?
                    reverse = []
                    break
                if matrix[nx][ny] == 0: # 빈 칸을 만난경우 reverse를 초기화
                    reverse = [] 
                    break
                if matrix[nx][ny]==c: # 같은 색을 만났으므로 break
                    break
                else: # 조건에 부합하는 돌을 reverse에 추가한다.
                    reverse.append((nx,ny))
                nx, ny = nx + dx, ny + dy
            for rx, ry in reverse: # 뒤집어준다.
                if c == 1:
                    matrix[rx][ry] = 1
                else:
                    matrix[rx][ry] = 2
        matrix[x][y] = c
    w, b = 0, 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                w += 1
            elif matrix[i][j] == 2:
                b += 1
     
    print('#{} {} {}'.format(test_case, w, b))