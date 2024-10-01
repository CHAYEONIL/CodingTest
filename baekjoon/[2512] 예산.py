import sys

sys = sys.stdin.readline

N = int(input())
arr= list(map(int, input().split()))
max_num = int(input())
sum = 0

# 상한액이 x일 때 필요한 금액
def calculate(x):
    ret = 0
    for i in range(N):
        ret += min(x, arr[i])
    return ret

left = 1
right = max(arr)
answer = -1

while left <= right:
    mid = (left + right) // 2

    if calculate(mid) <= max_num:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
