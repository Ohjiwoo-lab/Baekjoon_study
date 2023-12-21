from collections import deque

def solution(s):
    answer = 0
    n=len(s)
    
    q = deque(s)
    for _ in range(n):
        stack=[]    
        for j in range(n):
            if len(stack)==0:
                stack.append(q[j])
            elif stack[-1]=="(" and q[j]==")":
                stack.pop()
            elif stack[-1]=="{" and q[j]=="}":
                stack.pop()
            elif stack[-1]=="[" and q[j]=="]":
                stack.pop()
            else:
                stack.append(q[j])
        
        if len(stack)==0:
            answer+=1
        
        num = q.popleft()
        q.append(num)
        
    return answer