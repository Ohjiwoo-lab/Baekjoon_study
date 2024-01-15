def solution(board, h, w):
    answer = 0
    
    n1, n2 = len(board), len(board[0])
    row = [1,0,-1,0]
    col = [0,1,0,-1]
    
    for i in range(4):
        if 0<=h+col[i]<n1 and 0<=w+row[i]<n2 and board[h+col[i]][w+row[i]]==board[h][w]:
            answer+=1
    
    return answer