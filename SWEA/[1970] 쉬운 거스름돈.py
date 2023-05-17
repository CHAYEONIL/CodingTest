T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    list = [0] * 8
    for i in range(8):
        if N // money[i] != 0:
            list[i] = N//money[i] # 몫
            N = N % money[i] # 나머지
    
    print("#{}".format(test_case))
    print(*list)
    