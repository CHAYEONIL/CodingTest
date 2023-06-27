n = int(input())
list_n = list(map(int, input().split()))
b,c = map(int, input().split())
cnt = 0
# 각 방마다 총감독관 인원수 빼고 부감독관 인원수만큼 투입

for i in range(n):
    temp = list_n[i] - b
    cnt += 1

    if temp > 0:
        if temp & b:
            cnt += (temp // b) + 1
        else:
            cnt += (temp // b)

print(cnt)
