def solution(wallpaper):
    answer = []
    
    addr_x, addr_y=[],[]
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if wallpaper[i][j]=="#":
                addr_x.append(i)
                addr_y.append(j)
    answer=[min(addr_x),min(addr_y),max(addr_x)+1,max(addr_y)+1]
    
    return answer