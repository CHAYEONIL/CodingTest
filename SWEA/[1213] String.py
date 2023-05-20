T = int(input())

for test_case in range(1, T+1):
    string1 = input()
    string2 = input()

    count = string2.count(string1)
    print(count)