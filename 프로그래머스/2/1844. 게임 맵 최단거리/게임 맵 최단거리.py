from collections import deque

def bfs(x,y,maps,n,m):
    answer = -1
    
    queue=deque()
    queue.append([x,y,1])
    
    visited=[]
    for i in range(m):
        tmp=[]
        for j in range(n):
            tmp.append(False)
        visited.append(tmp)
    
    row=[1,0,-1,0]
    col=[0,1,0,-1]
    while queue:
        x,y,cnt=queue.popleft()
        if x==m-1 and y==n-1:
            answer=cnt
            break
        
        for i in range(4):
            if 0<=x+col[i]<m and 0<=y+row[i]<n and maps[x+col[i]][y+row[i]]!=0 and not visited[x+col[i]][y+row[i]]:
                queue.append([x+col[i],y+row[i],cnt+1])
                visited[x+col[i]][y+row[i]]=True
    
    return answer

def solution(maps):
    n,m=len(maps[0]),len(maps)
    answer = bfs(0,0,maps,n,m)
    
    return answer