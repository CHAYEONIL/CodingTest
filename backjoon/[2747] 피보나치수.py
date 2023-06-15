N = int(input())

array = [0, 1]
for i in range(2, N+1):
    array.append(array[-1] + array[-2])

print(array[N])