# 탑

from sys import stdin

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        
    def getSize(self):
        return self.size
    
    def stack_push(self, index, num):
        self.stack.append((index,num))
        self.size += 1
    
    def stack_pop(self):
        if self.size==0:
            return -1
        else:
            index, num = self.stack.pop()
            self.size -= 1
            return index
    
    def stack_peek(self):
        if self.size==0:
            return -1
        else:
            return self.stack[-1]


n = int(stdin.readline())
n_list = list(map(int, stdin.readline().split()))

stack = Stack()
result = [0]*n

for i in range(n):
    if stack.getSize() == 0:
        stack.stack_push(i,n_list[i])
        continue

    index, num = stack.stack_peek()
    if num > n_list[i]:
        result[i] = index+1
        stack.stack_push(i, n_list[i])
        
    else:
        while True:
            stack.stack_pop()
            if stack.getSize() == 0:
                stack.stack_push(i,n_list[i])
                break
            index, num = stack.stack_peek()
            if num > n_list[i]:
                result[i] = index+1
                stack.stack_push(i, n_list[i])
                break
        
for i in result:
    print(i, end=" ")