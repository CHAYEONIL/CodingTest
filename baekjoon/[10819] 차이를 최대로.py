from itertools import permutations
import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ans = -1

for p in list(permutations(a)) :
    sum = 0
    for i in range(N - 1) :
        sum += abs(p[i] - p[i - 1])
    
    if ans < sum :
        ans = sum

print(ans)