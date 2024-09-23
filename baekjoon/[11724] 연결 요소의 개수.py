import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1

    graph[u].append(v)
    graph[v].append(u)

visit = [False] * N
queue = deque()

count = 0
for i in range(N):
    if not visit[i]:
        queue.append(i)
        visit[i] = True
    
    # bfs
        while len(queue) != 0:
            u = queue.popleft()

            for v in graph[u]:
                if not visit[v]:
                    queue.append(v)
                    visit[v] = True

        count += 1

print(count)