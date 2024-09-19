# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 스택은 후입선출
import sys
input=sys.stdin.readline

n = int(input())
stack = []

def push(x): #리스트 마지막에 추가
    stack.append(x)

def pop(): #가장 위에 있는 정수 출력 없으면 -1
    if(len(stack)==0):
        print(-1)
    else:
        print(stack.pop())

def size(): #정수의 개수 출력
    print(len(stack))

def empty():
    if(len(stack)==0): #비면
        print(1)
    else: #안비면
        print(0)

def top():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack[-1])

for i in range(n):
    command = input().split()
    if (command[0] == 'push'):
        push(command[1])
    if (command[0] == 'pop'):
        pop()
    if (command[0] == 'size'):
        size()
    if (command[0] == 'empty'):
        empty()
    if (command[0] == 'top'):
        top()