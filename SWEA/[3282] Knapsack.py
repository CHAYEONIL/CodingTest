T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = []
    V = []
    C = []
    for _ in range(N):
        B1, B2 = (map(int, input().split()))
        A.append(B1)
        A.append(B2)
    for i in range(len(A)):
        if i % 2 == 0:
            V.append(A[i])
        else:
            C.append(A[i])
    
    print(V)
    print(C)