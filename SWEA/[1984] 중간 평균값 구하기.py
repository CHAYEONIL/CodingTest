T = int(input())

for test_case in range(1, T+1):
    soo = list(map(int, input().split()))
    soo.sort()
    soo.pop(9)
    soo.pop(0)
    plus = 0
    for i in range(len(soo)):
        plus += soo[i]
    answer = round(plus/8)

    print("#{} {}".format(test_case, answer))
