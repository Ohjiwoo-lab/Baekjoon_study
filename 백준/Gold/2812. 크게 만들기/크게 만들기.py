# 골드 3 - 크게 만들기

from sys import stdin

n,k=map(int, stdin.readline().strip().split())
num=stdin.readline().strip()

stack=[]
cnt=0
for i in num:
    if cnt<k:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] >= i:
                stack.append(i)
            else:
                while stack:
                    if cnt >= k:
                        break
                    if stack[-1] < i:
                        stack.pop()
                        cnt += 1
                    else:
                        break

                stack.append(i)
    else:
        stack.append(i)

for i in range(k-cnt):
    stack.pop()

for i in stack:
    print(i,end="")