import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

psum = [0] * N
psum[0] = arr[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + arr[i]

count = {}
answer = 0

for i in range(N):
    goal = psum[i] - M

    if goal in count:
        answer += count[goal]
    if goal == 0:
        answer += 1
    
    if psum[i] not in count:
        count[psum[i]] = 0
    count[psum[i]] += 1

print(answer)