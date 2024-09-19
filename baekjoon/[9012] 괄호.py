# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS
# 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 
# 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 
# “(()” 는 모두 VPS 가 아닌 문자열

n = int(input()) 
for i in range(n):
    VPSs = input()
    List_VPS = list(VPSs)
    sum = 0 # 판별하기 위한 합, 합이 0이어야 VPS!

    for i in List_VPS:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0: # SUM이 -1이 되어 조건을 충족못하면 break
            print('NO')
            break
    
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')