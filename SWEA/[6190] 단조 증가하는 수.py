def chkIncrease(number):
    number_string = str(number)
    for k in range(len(number_string) - 1):
        if number_string[k] > number_string[k+1]:
            return False
    return True

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    maxNum = 0

    for i in range(N-1):
        for j in range(i+1, N):
            num = A[i] * A[j]
            if chkIncrease(num):
                maxNum = max(maxNum, num)
    if maxNum == 0:
        maxNum = -1
    
    print("#{} {}".format(test_case, maxNum))
