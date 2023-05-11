def find_best_taste(N, L, T, K):
    dp = [[0] * (L+1) for _ in range(N+1)] # 각 재료마다 선택 여부에 따른 맛의 합 저장

    for i in range(1, N+1):
        for j in range(1, L+1):
            if K[i-1] > j: # 현재 선택하는 재료의 칼로리가 제한 칼로리보다 크면
                dp[i][j] = dp[i-1][j] # 이전에 저장한 합을 이용하여 현재 선택하지 않는 경우의 맛의 합을 계산
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-K[i-1]] + T[i-1]) # 현재 선택하는 재료를 선택하는 경우와 선택하지 않는 경우 중에서 더 높은 맛의 합을 저장

    return dp[N][L] # 제한 칼로리 이하의 최댓값 반환


T = int(input()) # 테스트 케이스의 수

for test_case in range(1, T+1):
    N, L = map(int, input().split())
    T, K = [], []
    for i in range(N):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
    ans = find_best_taste(N, L, T, K)
    print("#{} {}".format(test_case, ans))