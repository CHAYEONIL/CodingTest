N, K = map(int, input().split())
monster = list(map(int, input().split()))
npc = list(map(int, input().split()))
visited = [False for _ in range(N)]
save = 0 # 구한 사람 수

def solution(cur, damage, saved):
    global save
    save = max(save, saved)

    if not cur:
        return
    
    remain = sum([npc[i] for i in range(N) if not visited[i] and damage+ monster[i] <= cur])

    if saved + remain <= save:
        return

    for i in range(N):
        if not visited[i] and damage + monster[i] <= cur:
            visited[i] = True
            solution(cur - damage - monster[i] , damage + monster[i], saved + npc[i])
            visited[i] = False

solution(K, 0, 0)
print(save)