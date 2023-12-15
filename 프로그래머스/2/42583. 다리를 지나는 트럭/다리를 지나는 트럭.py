from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer,w = 1,0
    
    q=deque()   # 현재 다리에 있는 트럭
    truck=deque(truck_weights)  # 대기 중인 트럭 리스트
    
    while truck or q:
        if q and (answer-q[0][0])==bridge_length:
            _,num=q.popleft()
            w-=num
        
        if truck:
            if len(q) >= bridge_length:
                answer+=1
            elif (w+truck[0])>weight:
                answer+=1
            else:
                num=truck.popleft()
                q.append([answer,num])
                w+=num
                answer+=1
        elif q:
            answer+=1
        else:
            break
            
    return answer