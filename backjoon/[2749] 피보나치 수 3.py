# 피사노 주기
# 주기의 길이가 P이면 N번째 피보나치 수를 M으로 나눈 나머지=(N% P) 번째 피보나치 수를 M을 나눈 나머지

M = 1000000
P = 1500000

N = int(input())

def fibo(n):
    a, b = 0, 1

    for _ in range(n):
        a , b = b % M, (a+b) % M
    return a

print(fibo(N % P))