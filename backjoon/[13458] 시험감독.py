import math

n = int(input())
list_n = list(map(int, input().split()))
b,c = map(int, input().split())
cnt = n
# 각 방마다 총감독관 인원수 빼고 부감독관 인원수만큼 투입

for i in list_n:
    #올림 처리 + max를 사용해서 음수의경우 0이 되도록 처리
    cnt += max(math.ceil((i-b)/c),0)

print(cnt)