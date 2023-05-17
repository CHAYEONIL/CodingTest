T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    queue = list(map(int, input().split()))

    cnt = 1
    while True:
        if cnt > 5:
            cnt = 1
        t = queue.pop(0) - cnt
        if t <= 0:
            queue.append(0)
            break
        queue.append(t)
        cnt += 1

    print("#{} {} {} {} {} {} {} {} {}".format(tc, *queue))