my_dict = {'0001101': 0, '0011001': 1,
           '0010011': 2, '0111101': 3,
           '0100011': 4, '0110001': 5,
           '0101111': 6, '0111011': 7,
           '0110111': 8, '0001011': 9}

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    mycode = ''
    for i in range(N):
        if sum(map(int, list(arr[i]))) == 0:
            continue
        else:
            v_code = arr[i]
            for j in range(M-1, -1, -1) :
                if v_code[j] == '1':
                    mycode = v_code[j-55:j+1]
                    break
            break
    mycodelist = [my_dict[mycode[i:i+7]] for i in range(0, 56, 7)]
    odd = 0
    even = 0
    for i in range(7):
        if i % 2:
            even += mycodelist[i]
        else:
            odd += mycodelist[i]
    
    answer = odd * 3 + even + mycodelist[-1]
    print("#{}".format(test_case), end = ' ')
    if answer % 10 == 0:
        print(sum(mycodelist))
    else:
        print(0)