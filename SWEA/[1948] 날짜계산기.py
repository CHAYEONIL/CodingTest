T = int(input())

for test_case in range(1, T + 1):
    fm, fd, sm, sd = map(int,input().split())
    month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    answer = 0
    for i in range(fm, sm) :
        if fm == i :
            answer += month[i] - fd + 1
        else :
            answer += month[i]
    answer += sd
    print("#{} {}".format(test_case, answer))

