# 브론즈 1 - 캠핑

i = 1
while True:
    p,l,v=map(int,input().split())
    if p==0 and l==0 and v==0:
        break

    answer=0
    n=v//l
    m=v%l
    answer+=n*p

    if m<p:
        answer+=m
    else:
        answer+=p

    print(f"Case {i}: ",end="")
    print(answer)
    i+=1