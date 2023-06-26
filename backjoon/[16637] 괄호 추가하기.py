import sys

T = int(input())
S = input()
result = -1 * sys.maxsize

def Operator(num1, op, num2):
    if op == "+" :
        return num1 + num2
    if op == "-" :
        return num1 - num2
    if op == "*" :
        return num1 * num2

def dfs(index, value):
    global result

    if index == T - 1:
        result = max(result, value)
        return
    
    if index + 2 < T:
        dfs(index + 2, Operator(value, S[index + 1], int(S[index + 2])))

    if index + 4 < T:
        dfs(index + 4, Operator(value, S[index + 1], Operator(int(S[index + 2]), S[index + 3], int(S[index + 4]))))

dfs(0, int(S[0]))
print(result)