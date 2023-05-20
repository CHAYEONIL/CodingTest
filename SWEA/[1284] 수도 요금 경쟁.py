T = int(input())

for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    N1 = P * W
    N2 = 0

    if W <= R:
        N2 = Q
    else:
        N2 = Q + S * (W - R)

    if N1 <= N2:
        print("#{} {}".format(test_case, N1))
    else:
        print("#{} {}".format(test_case, N2))