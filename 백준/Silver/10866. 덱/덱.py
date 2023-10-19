from collections import deque
from sys import stdin

n = int(stdin.readline().strip())

queue=deque()
for i in range(n):
    op = list(stdin.readline().strip().split())
    if op[0]=="push_front":
        queue.appendleft(int(op[1]))
    elif op[0]=="push_back":
        queue.append(int(op[1]))
    elif op[0]=="pop_front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif op[0]=="pop_back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop())
    elif op[0]=="size":
        print(len(queue))
    elif op[0]=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif op[0]=="front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif op[0]=="back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    else:
        print("잘못된 명령어를 입력하였습니다.")