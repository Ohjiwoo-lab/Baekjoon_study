from sys import stdin

s=stdin.readline().strip()
bomb=stdin.readline().strip()
n1,n2=len(s),len(bomb)-1

stack=[]
for i in range(n1):
    if n2==0 and s[i]==bomb:
        continue
    
    if len(stack)==0:
        stack.append(s[i])
        continue
    
    flag=True
    if len(stack)>=(n2-1) and s[i]==bomb[n2]:
        for j in range(1,n2+1):
            if stack[len(stack)-j]!=bomb[n2-j]:
                stack.append(s[i])
                flag=False
                break
        if flag:
            del stack[len(stack)-n2:]
    else:
        stack.append(s[i])

if len(stack)==0:
    print("FRULA")
else:
    for i in stack:
        print(i,end="")
    print()