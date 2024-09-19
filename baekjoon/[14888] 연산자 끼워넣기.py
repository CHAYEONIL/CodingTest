N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

maxi = -1e9
mini = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maxi, mini

    if depth == N:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    
    if plus:
        dfs(depth + 1 , total + A[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1 , total - A[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1 , total * A[depth], plus , minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1 , int(total / A[depth]), plus , minus, multiply, divide - 1)
    
dfs(1, A[0], op[0], op[1], op[2], op[3])
print(maxi)
print(mini)