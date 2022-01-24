# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

def fibo(n) :
    if n <= 1 :
        return n
    else :
        return fibo(n-2) + fibo(n-1)

print(fibo(int(input())))