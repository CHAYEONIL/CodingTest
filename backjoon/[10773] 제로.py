K = int(input())
answer = []

for i in range(K):
    n = int(input())
    if n == 0:
        answer.pop()
    else:
        answer.append(n)

print(sum(answer))
