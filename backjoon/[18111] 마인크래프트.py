import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

min_value = min(map(min,arr))
max_value = max(map(max,arr))
min_time = 1e9

for i in range(min_value, max_value + 1):
    pcnt = 0
    mcnt = 0
    for j in range(N):
        for k in range(M):
            h = arr[j][k] - i
            if h > 0:
                mcnt += h
            elif h < 0: # h가 음수라서 -
                pcnt -= h
    if mcnt + B >= pcnt:
        time = mcnt * 2 + pcnt

        if min_time >= time:
            min_time = time
            result = i

print(min_time, result)