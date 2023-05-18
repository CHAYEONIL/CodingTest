T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dct = {}
r_dct = {}
i, j = 1, 1
for n in range(1, 50000): #10000까지의 숫자를 좌표에 저장할 때, 그 4배의 크기 삼각형
    dct[n] = (i,j)
    r_dct[(i,j)] = n
    i, j = i-1, j+1
    if i<1:
        i, j = j, 1
for test_case in range(1, T + 1):
    p, q = map(int, input().split())

    pi, pj = dct[p]
    qi, qj = dct[q]

    answer = r_dct[(pi+qi, pj+qj)]
    print("#{} {}".format(test_case, answer))
