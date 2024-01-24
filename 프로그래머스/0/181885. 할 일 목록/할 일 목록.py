def solution(todo_list, finished):
    answer = []
    
    for i, flag in enumerate(finished):
        if not flag:
            answer.append(todo_list[i])
    
    return answer