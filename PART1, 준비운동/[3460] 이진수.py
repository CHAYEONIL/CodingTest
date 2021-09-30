# 양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오.
# 최하위 비트(least significant bit, lsb)의 위치는 0이다.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. (1 ≤ T ≤ 10, 1 ≤ n ≤ 106)

T = int(input())
 
for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i - 1] == '1':
            print(i, end=' ')
