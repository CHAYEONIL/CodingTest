T = 10

for test_case in range(1, T+1):
    N = int(input())
    string1 = input()
    string2 = input()

    count = string2.count(string1)
    print("#{} {}".format(N, count))