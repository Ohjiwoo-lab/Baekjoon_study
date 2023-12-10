from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for trees in skill_trees:
        q=deque(skill)
        flag=True
        for tree in trees:
            if tree in skill and q:
                if q[0]==tree:
                    q.popleft()
                else:
                    flag=False
                    break
        if flag:
            answer+=1
    
    return answer