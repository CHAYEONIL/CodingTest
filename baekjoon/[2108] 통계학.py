import sys
from collections import Counter

n = int(sys.stdin.readline())

num = []
for _ in range(n) :
    num.append(int(sys.stdin.readline()))

# 산술평균
average = round(sum(num) / n)
print(average)

# 중앙값
num.sort()
print(num[int((n-1)/2)])

# 최빈값
"""
counts = dict()
for i in range(1, n+1) :
    counts[i] = []

maxCount = 1
count = 1
for j in range(1,n):
    if num[j] == num[j-1] :
        count += 1
    else :
        counts[count].append(num[j-1])
        if maxCount < count :
            maxCount = count
    if j == n-1 :
        counts[count].append(num[j])
        if maxCount < count :
            maxCount = count
if n == 1 :
    counts[1].append(num[0])

counts[maxCount].sort()
if len(counts[maxCount]) == 1 :
    print(counts[maxCount][0])
else :
    print(counts[maxCount][1])
"""
cnt_li = Counter(num).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1] : #최빈값이 두개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
# 범위
print(num[-1] - num[0])