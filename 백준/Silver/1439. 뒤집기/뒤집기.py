s=input()

a=s.split('0')
b=s.split('1')

cnt1,cnt2=0,0
for i in a:
    if i=="":
        continue
    else:
        cnt1+=1
        
for i in b:
    if i=="":
        continue
    else:
        cnt2+=1

print(min(cnt1,cnt2))