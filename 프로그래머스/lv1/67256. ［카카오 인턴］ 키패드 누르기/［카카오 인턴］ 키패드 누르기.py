def solution(numbers, hand):
    answer = ''
    
    key=[[3,1],[0,0],[0,1],[0,2],
        [1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    
    left,right=[3,0],[3,2]
    
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            left=key[i]
        elif i in [3,6,9]:
            answer+='R'
            right=key[i]
        else:
            x,y=key[i][0],key[i][1]
            if abs(x-left[0])+abs(y-left[1])>abs(x-right[0])+abs(y-right[1]):
                answer+='R'
                right=key[i]
            elif abs(x-left[0])+abs(y-left[1])<abs(x-right[0])+abs(y-right[1]):
                answer+='L'
                left=key[i]
            else:
                if hand=="right":
                    answer+='R'
                    right=key[i]
                else:
                    answer+='L'
                    left=key[i]
    
    return answer