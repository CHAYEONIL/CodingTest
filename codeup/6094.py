# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

n = int(input())
num_list = map(int, input().split())

list_min = min(num_list)
print(list_min)