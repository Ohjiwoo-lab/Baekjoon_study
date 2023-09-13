def solution(rank, attendance):
    answer = 0
    
    rank_list = []
    for i in range(len(rank)):
        if attendance[i]:
            rank_list.append([i, rank[i]])
    
    rank_list.sort(key=lambda x:x[1])
    
    a=rank_list[0][0]
    b=rank_list[1][0]
    c=rank_list[2][0]
    answer = 10000*a + 100*b + c
    
    return answer