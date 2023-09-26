def solution(board, moves):
    answer = 0
    
    box = []
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                if len(box)!=0 and box[len(box)-1]==j[i-1]:
                    box.pop()
                    answer += 2
                else:
                    box.append(j[i-1])
                j[i-1]=0
                break

    return answer