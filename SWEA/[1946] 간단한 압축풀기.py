T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    value = ""
    for tc in range(1, N+1):
        al, soo = input().split()
        soo = int(soo)
        value += al * soo

    print("#{}".format(test_case))
    for i in range(len(value)):
        if (i+1)%10 == 0:
            print(value[i])
        else:
            print(value[i], end = "")
    print()