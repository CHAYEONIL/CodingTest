# 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 
# 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성
# 스택에 push하는 순서는 반드시 오름차순
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지

n = int(input())
stack = []
answer = []
count = 1
temp = True

for i in range(n):
    stack_num = int(input())
    while count <= stack_num: # 입력한 수를 만날 때까지 오름차순으로 push
        stack.append(count)
        answer.append('+')
        count += 1
    # 입력한 수를 만나면 while문 탈출

    if stack[-1] == stack_num:
        stack.pop()
        answer.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in answer:
        print(i)

