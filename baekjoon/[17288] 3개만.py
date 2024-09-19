# 첫째 줄에 문자열 S(3 ≤ S의 길이 ≤ 100)가 주어진다.
# 연속된 세 숫자가 등장한 횟수를 출력한다.

import sys

input = sys.stdin.readline

S = list(map(int, input().rstrip()))
result = str(S[0])
cnt = 0

for i in range(1, len(S) + 1):
    if i == len(S):
        if len(result) == 3:
            print(cnt + 1)
            sys.exit(0)
        print(cnt)
        sys.exit(0)

    if S[i - 1] == S[i] - 1:
        result += str(S[i])

    else:
        if len(result) == 3:
            cnt += 1
        result = ''
        result += str(S[i])

print(cnt)
