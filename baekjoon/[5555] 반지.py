# 찾고자하는 문자열이 주어졌을 때 그 문자열을 포함하는 반지가 몇 개인지를 발견하는 프로그램을 작성하라.

ring_string = input()

N = int(input())
count = 0 #변수 초기화

for _ in range(N) :
    ring = input()
    ring += ring

    if ring.find(ring_string) != -1:
        count += 1
    

print(count)