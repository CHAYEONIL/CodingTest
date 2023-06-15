T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    dp = [[0] * (K+1) for _ in range(N+1)]
    items = [list(map(int,input().split())) for _ in range(N)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            if items[i - 1][0] <= j:
                dp[i][j] = max(dp[i - 1][j], items[i - 1][1] + dp[i - 1][j - items[i - 1][0]])
            else:
                dp[i][j] = dp[i - 1][j]
    print("#{} {}".format(test_case, dp[N][K]))