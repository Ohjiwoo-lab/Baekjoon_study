# 스택
from sys import stdin

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def stack_push(self, x):
        self.stack.append(x)
        self.size += 1

    def stack_pop(self):
        if self.size == 0:
            return -1
        else:
            data = self.stack.pop()
            self.size -= 1
            return data

    def stack_size(self):
        return self.size

    def stack_empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def stack_top(self):
        if self.size == 0:
            return -1
        else:
            return self.stack[-1]

N = int(stdin.readline())
stack = Stack()

for i in range(N):
    operation = stdin.readline().split()

    if operation[0] == 'push':
        stack.stack_push(operation[1])
    elif operation[0] == 'pop':
        print(stack.stack_pop())
    elif operation[0] == 'size':
        print(stack.stack_size())
    elif operation[0] == 'empty':
        print(stack.stack_empty())
    elif operation[0] == 'top':
        print(stack.stack_top())
    else:
        print('잘못된 연산을 입력하셨습니다.')