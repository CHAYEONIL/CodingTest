# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

n = int(input())

for i in range(n):
    sentence = list(input().split())
    for j in sentence:
        print(j[::-1], end = ' ') # ' ' 을 통해 값을 구분