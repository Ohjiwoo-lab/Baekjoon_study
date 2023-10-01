def solution(park, routes):
    answer = []
    
    h=len(park)
    w=len(park[0])
    location,no=[],[]
    for i in range(h):
        for j in range(w):
            if park[i][j]=="S":
                location=[i,j]
            if park[i][j]=="X":
                no.append([i,j])
    
    for step in routes:
        op,n=step.split()
        n=int(n)
        flag=False
        if op=="N":
            x,y=location[0]-n,location[1]
            if x<0:
                continue
            for i in range(1,n+1):
                if [location[0]-i,y] in no:
                    flag=True
                    break
            if flag:
                continue
            location=[x,y]
        elif op=="S":
            x,y=location[0]+n,location[1]
            if x>=h:
                continue
            for i in range(1,n+1):
                if [location[0]+i,y] in no:
                    flag=True
                    break
            if flag:
                continue
            location=[x,y]
        elif op=="W":
            x,y=location[0],location[1]-n
            if y<0:
                continue
            for i in range(1,n+1):
                if [x,location[1]-i] in no:
                    flag=True
                    break
            if flag:
                continue
            location=[x,y]
        else:
            x,y=location[0],location[1]+n
            if y>=w:
                continue
            for i in range(1,n+1):
                if [x,location[1]+i] in no:
                    flag=True
                    break
            if flag:
                continue
            location=[x,y]

    answer=location
    
    return answer