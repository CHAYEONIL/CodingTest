from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    c = [[-1] * (W + 2) for _ in range(H + 2)]
    q.append([x, y])
    c[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H+2 and 0 <= ny < W+2:
                if c[nx][ny] == -1:
                    if a[nx][ny] == '.':
                        c[nx][ny] = c[x][y]
                        q.appendleft([nx, ny])
                    elif a[nx][ny] == '#':
                        c[nx][ny] = c[x][y] + 1
                        q.append([nx, ny])

    return c

T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    a = [list(input().strip()) for _ in range(H)]
    q = deque()

    for i in a:
        i.insert(0, '.')
        i.append('.')
    a.insert(0, ['.' for _ in range(W+2)])
    a.append(['.' for _ in range(W+2)])

    temp = []
    for i in range(H + 2):
        for j in range(W + 2):
            if a[i][j] == '$':
                temp.extend([i, j])
                a[i][j] = '.'

    x1, y1, x2, y2 = temp
    c1 = bfs(0, 0)
    c2 = bfs(x1, y1)
    c3 = bfs(x2, y2)

    ans = sys.maxsize
    for i in range(H+2):
        for j in range(W+2):
            if c1[i][j] != -1 and c2[i][j] != -1 and c3[i][j] != -1:
                cnt = c1[i][j] + c2[i][j] + c3[i][j]
                if a[i][j] == '#':
                    cnt -= 2
                ans = min(ans, cnt)
    print(ans)