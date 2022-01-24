# 기차보다 빠른 비행기를 타기 위해 더 많은 돈을 지불하는것이 과연 그만한 가치가 있는 것일까?
#거리 M(Km)이 주어졌을때 기차의 속도 A(Km/h)와 비행기의 속도 B(Km/h)로 달렸을때 발생하는 시간의 차를 계산하여라.

while 1:
    M, A, B = map(int, input().split())

    if M == A == B == 0:
        break

    take_time = round((M/A - M/B)*3600)
    h = take_time // 3600
    m = take_time - h * 3600
    mm = m // 60
    ss = m - mm*60

    print("%d:%02d:%02d" % (h, mm, ss))
