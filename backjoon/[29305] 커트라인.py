n, p = map(int, input().split())
x = list(map(int,input().split()))

x.sort(reverse = True)
print(x[p-1])