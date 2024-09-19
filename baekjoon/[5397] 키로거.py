# 강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오. 
# 강산이는 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표이다.


N = int(input())

for i in range(N):
    left = []
    right = []
    pwd = input()

    for j in pwd:
        if j == "-":
            if left:
                left.pop()
        elif j == "<":
            if left:
                right.append(left.pop())
        elif j == ">":
            if right:
                left.append(right.pop())
        else:
            left.append(j)

    left.extend(reversed(right))
    print("".join(left))