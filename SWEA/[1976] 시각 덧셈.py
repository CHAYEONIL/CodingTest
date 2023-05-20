T = int(input())

for test_case in range(1, T+1):
    hour1, min1, hour2, min2 = map(int, input().split())

    hour = hour1 + hour2
    min = min1 + min2

    if min > 60:
        hour += 1
        min -= 60
    if hour > 12:
        hour -= 12
    
    print("#{} {} {}".format(test_case, hour, min))