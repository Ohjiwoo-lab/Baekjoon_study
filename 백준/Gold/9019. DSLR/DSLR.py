# 골드 4 - DSLR

from collections import deque
from sys import stdin

def bfs(q, visited, b):
    while q:
        num, op = q.popleft()
        if num == b:
            print(op)
            break

        # 1번 연산
        if num*2 >= 10000:
            if not visited[(num*2)%10000]:
                q.append([(num*2)%10000, op+'D'])
                visited[(num*2)%10000] = True
        else:
            if not visited[num * 2]:
                q.append([num*2, op+'D'])
                visited[num*2] = True

        # 2번 연산
        if num-1 < 0:
            if not visited[9999]:
                q.append([9999, op+'S'])
                visited[9999] = True
        else:
            if not visited[num-1]:
                q.append([num-1, op+'S'])
                visited[num-1] = True

        # 3번 연산
        n = len(str(num))-1
        if n==3:
            strNum = (num%(10**n))*10 + num//(10**n)
        else:
            strNum = num*10

        if not visited[strNum]:
            q.append([strNum, op + 'L'])
            visited[strNum] = True

        # 4번 연산
        strNum2 = (num%10)*(10**3) + num//10
        if not visited[strNum2]:
            q.append([strNum2, op+'R'])
            visited[strNum2] = True

t = int(stdin.readline())
for i in range(t):
    a, b = map(int, stdin.readline().strip().split())

    q = deque()
    q.append([a, ''])

    visited = [False]*10000
    visited[a] = True

    bfs(q, visited, b)