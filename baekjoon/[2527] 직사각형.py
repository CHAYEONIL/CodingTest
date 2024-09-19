for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    left_large = max(x1, x2)
    right_small = min(p1, p2)
    down_small = min(q1, q2)
    up_large = max(y1, y2)

    xdiff = right_small - left_large
    ydiff = down_small - up_large

    if xdiff > 0 and ydiff > 0:
        print('a')
    elif xdiff < 0 or ydiff < 0:
        print('d')
    elif xdiff == 0 and ydiff == 0:
        print('c')
    else:
        print('b')