def solution(places):
    answer = []
    
    n=5
    for place in places:
        flag=False
        for i in range(n):
            for j in range(n):
                # 차례대로 앉아있는 사람을 검사
                if place[i][j]=="P":
                    # 1. 오른쪽 옆
                    if (j+1)<n and place[i][j+1]=="P":
                        flag=True
                        break
                    # 2. 오른쪽 옆옆
                    if (j+2)<n and place[i][j+1]=="O" and place[i][j+2]=="P":
                        flag=True
                        break
                    # 3. 왼쪽 옆
                    if (j-1)>=0 and place[i][j-1]=="P":
                        flag=True
                        break
                    # 4. 왼쪽 옆옆
                    if (j-2)>=0 and place[i][j-1]=="O" and place[i][j-2]=="P":
                        flag=True
                        break    
                    # 5. 아래
                    if (i+1)<n and place[i+1][j]=="P":
                        flag=True
                        break
                    # 6. 아래 아래
                    if (i+2)<n and place[i+1][j]=="O" and place[i+2][j]=="P":
                        flag=True
                        break
                    # 7. 위
                    if (i-1)>=0 and place[i-1][j]=="P":
                        flag=True
                        break
                    # 8. 위위
                    if (i-2)>=0 and place[i-1][j]=="O" and place[i-2][j]=="P":
                        flag=True
                        break
                    # 9. 오른쪽 위 대각선
                    if (i-1)>=0 and (j+1)<n and place[i-1][j+1]=="P":
                        if place[i-1][j]=="O" or place[i][j+1]=="O":
                            flag=True
                            break
                    # 10. 오른쪽 아래 대각선
                    if (i+1)<n and (j+1)<n and place[i+1][j+1]=="P":
                        if place[i+1][j]=="O" or place[i][j+1]=="O":
                            flag=True
                            break
                    # 11. 왼쪽 위 대각선
                    if (i-1)>=0 and (j-1)>=0 and place[i-1][j-1]=="P":
                        if place[i-1][j]=="O" or place[i][j-1]=="O":
                            flag=True
                            break
                    # 12. 왼쪽 아래 대각선
                    if (i+1)<n and (j-1)>=0 and place[i+1][j-1]=="P":
                        if place[i+1][j]=="O" or place[i][j-1]=="O":
                            flag=True
                            break
            
            if flag:
                break
        
        if flag:
            answer.append(0)
        else:
            answer.append(1)
            
    return answer