import math
T = int(input())

for test_case in range(1, T+1):
    N, R = map(int, input().split())
    R_fac = math.factorial(R)
    N_list = []
    boonja = 1
    for i in range(N, 0, -1):
        N_list.append(i)
    for i in range(R):
        boonja *= N_list[i]

    answer = boonja / R_fac
    ans = math.floor(answer % 1234567891)

    print("#{} {}".format(test_case, ans))