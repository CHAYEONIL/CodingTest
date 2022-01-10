# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

n = int(input())
num_list = input().split()

num_list.reverse()

for i in range(n):
    print(num_list[i], end=' ')