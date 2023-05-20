T = 10

for test_case in range(1, T+1):
    N = int(input())
    answer = 1
    num, gop = map(int, input().split())

    for i in range(gop):
        answer *= num
    
    print("#{} {}".format(test_case, answer))