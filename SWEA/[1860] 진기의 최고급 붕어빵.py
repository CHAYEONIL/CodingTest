T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()

    answer = "Possible"
    for i in range(N):
        # x초까지 만들어진 붕어 개수: (x // M) * K
        boong = (arrive[i] // M) * K -(i+1)
        if boong < 0:
            answer = "Impossible"
            break
    
    print("#{} {}".format(test_case, answer))