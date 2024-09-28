import sys

input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
pa = [0]
tmp = 0

for i in a:
    tmp += i
    pa.append(tmp)

for _ in range(M):
    i, j = map(int, input().split())
    print(pa[j] - pa[i - 1])
