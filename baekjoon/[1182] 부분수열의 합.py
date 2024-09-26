from itertools import combinations
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(1, N + 1):
    for c in list(combinations(A, i)):
        if sum(c) == S:
            ans += 1

print(ans)