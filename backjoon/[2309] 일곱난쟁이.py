# 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

arr = []
for _ in range(9) :
    arr.append(int(input()))

arr.sort()
sum_arr = sum(arr)

for i in range(9) :
    for j in range(i+1, 9) :

        if sum_arr - (arr[i]+arr[j]) == 100 :
            for k in range(9) :
                if k == i or k == j :
                    continue
                else :
                    print(arr[k])
            exit()