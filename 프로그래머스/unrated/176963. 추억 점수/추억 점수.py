def solution(name, yearning, photo):
    answer = []
    
    for photo_list in photo:
        yearning_sum = 0
        for photo_name in photo_list:
            for i, n in enumerate(name):
                if photo_name == n:
                    yearning_sum += yearning[i]
                    break
        answer.append(yearning_sum)
            
    return answer