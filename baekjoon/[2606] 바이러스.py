N = int(input())
S = int(input())
warmlist = [[] for _ in range(N+1)]

for _ in range(S):
    direct1, direct2 = map(int, input().split())
    warmlist[direct1].append(direct2)
    warmlist[direct2].append(direct1)

def dfs(x):
    global cnt
    visited[x] = True
    cnt += 1
    for node in warmlist[x]:
        if visited[node]:
            continue
        dfs(node)

cnt = 0
visited = [False for _ in range(N+1)]
dfs(1)
print(cnt - 1)