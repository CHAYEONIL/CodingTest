N = int(input())

for _ in range(N):
    list_i = list(map(int, input().split()))
    mid = sum(list_i[1:]) / list_i[0]

    cnt = 0
    for score in list_i[1:]:
        if score > mid:
            cnt += 1

    rate = cnt/list_i[0] * 100
    print('%.3f' %rate + '%')