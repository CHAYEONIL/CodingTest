import sys
input = sys.stdin.readline

def count(data):
    Max = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if data[i][j] == data[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max,cnt)
        cnt = 1
        for j in range(1,n):
            if  data[j][i] == data[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max,cnt)

    return Max
    
n = int(input())
data = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
        	# 인점한 것과 바꾸기
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
            temp=count(data)
            ans = max(ans,temp)
            # 바꿨던 것을 다시 원래대로 돌려놓기
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
        # 행 바꾸기
        if i+1 < n:
        	# 인점한 것과 바꾸기
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
            temp=count(data)
            ans = max(ans,temp)
            # 바꿨던 것을 다시 원래대로 돌려놓기
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
print(ans)