T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = set()
    cnt = 1
    while True:
        for k in list(str(N)):
            arr.add(k)
        if len(arr) == 10:
            break
        N //= cnt
        cnt += 1
        N *= cnt
    
    print("#{} {}".format(test_case, N))