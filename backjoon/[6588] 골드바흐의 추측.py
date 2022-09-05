max = 1000001

check = [True for _ in range(max)]

#에라토스테네스의 체
for i in range(2, int((max-1)**0.5)+1):
    if check[i]:
        for k in range(i+i, max, i):
            check[k] = False

import sys
input = sys.stdin.readline

# 입력받은 수가 소수인지에 대한 확인
while(True):
    n = int(input())

    if n == 0:
        break

    flag = 0

    for i in range(3, len(check)):
        if check[i] and check[n-i]:
            print("%d = %d + %d" %(n, i, n-i))
            flag = 1
            break

    if flag == 0:
        print("Goldbach's conjecture is wrong.")
