# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

a = input()
alp = ord('a') # ord('a')는 유니코드 97
while True:
    print(chr(alp), end = ' ') #chr(97)은 알파벳 a

    if(chr(alp) == a):
        break;
    
    alp = alp + 1