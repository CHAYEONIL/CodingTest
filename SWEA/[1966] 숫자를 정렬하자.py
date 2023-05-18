T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    N_List = list(map(int,input().split()))
    N_List.sort()

    print("#{}".format(test_case), end = ' ')
    for i in range(N):
        print(N_List[i], end = ' ')
    print()