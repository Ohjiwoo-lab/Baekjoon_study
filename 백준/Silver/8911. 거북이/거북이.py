t=int(input())

dirx=[0,-1,0,1]
diry=[1,0,-1,0]
for i in range(t):
    d=0
    x,y=0,0
    min_x,max_x=0,0
    min_y,max_y=0,0
    move = input()
    for m in move:
        if m=='F':
            x+=dirx[d]
            y+=diry[d]
        if m=='B':
            x+=dirx[(d+2)%4]
            y+=diry[(d+2)%4]
        if m=='L':
            d=(d+1)%4
        if m=='R':
            d=(d+3)%4
        
        if x<min_x:
            min_x=x
        if x>max_x:
            max_x=x
        
        if y<min_y:
            min_y=y
        if y>max_y:
            max_y=y
 
    print((max_x-min_x)*(max_y-min_y))