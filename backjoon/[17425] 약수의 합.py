import sys

max = 1000000 # 최대값 설정

dp = [0] * (max + 1) # 각 인덱스 마다 약수의 합을 담아 놓을 배열

s = [0] * (max + 1) # 각 인덱스까지 누적합을 담을 배열

for i in range(1, max + 1) :
    j = 1 # i에 곱할 값
    while i * j <= max:
        dp[i * j] += i
        j += 1
    s[i] = s[i - 1] + dp[i]

n = int(input())

for _ in range(n):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(s[a])+"\n")