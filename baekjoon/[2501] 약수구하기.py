# 어떤 자연수 p와 q가 있을 떄, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

arr = []
N,K = map(int,input().split())
cnt = 0

for i in range(1, N+1) :
    if N % i == 0:
        arr.append(i)
    cnt += 1

if K> len(arr) :
    print(0)
else :
    print(arr[K-1])