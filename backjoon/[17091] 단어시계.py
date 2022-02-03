# 분 = 0이면 "o' clock"을 사용하고, 1 ≤ 분 ≤ 30은 "past"를, 30 < 분이면 "to" 를 사용한다.
# 시각이 주어졌을 때, 단어 시계에서 사용하는 표현으로 출력해보자.
# 첫째 줄에 시를 나타내는 h(1 ≤ h ≤ 12), 둘째 줄에 분을 나타내는 m(0 ≤ m < 60)이 주어진다.
# 예제 : 5 / 47 -> thirteen minutes to six
# 예제 : 7 / 15 -> quarter past seven

import sys

h = int(sys.stdin.readline())
m = int(sys.stdin.readline())

h_list = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'one'] 
        # 시간 부분 리스트, 런타임 에러떄문에 one한번 더 추가 -> 배열의 초과 방지
        
m_list = ['o\' clock', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 
            'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 
            'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 
            'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 
            'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half'] 
            #분 부분 리스트

def define(minute, hour, o_past_to, time_set):
    if minute == 1: # 1일떄는 minute로 출력 나머지는 minutes로 출력
        print('%s minute %s %s' % (m_list[minute], o_past_to, h_list[hour + time_set])) 
    elif minute == 15 or minute == 30:
        print('%s %s %s' % (m_list[minute], o_past_to, h_list[hour + time_set]))
    else:
        print('%s minutes %s %s' % (m_list[minute], o_past_to, h_list[hour + time_set]))

if m == 0:
    print('%s %s' % (h_list[h], m_list[m]))
elif 1 <= m and m <= 30:
    define(m, h, 'past', 0)
else:
    m = 60 - m
    define(m, h, 'to', 1)