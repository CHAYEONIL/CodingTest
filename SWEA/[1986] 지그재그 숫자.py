T = int(input())
for test_case in range(1, T + 1):
    value = int(input())
    answer = 0
    for i in range(1, value+1):
        if i % 2 != 0:
            answer += i
        else:
            answer -= i
    
    print("#{} {}".format(test_case, answer))