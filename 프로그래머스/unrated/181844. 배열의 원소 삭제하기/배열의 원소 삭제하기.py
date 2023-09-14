def solution(arr, delete_list):
    answer = []
    
    for delete_num in delete_list:
        if delete_num in arr:
            for i, num in enumerate(arr):
                if num==delete_num:
                    arr.pop(i)
    answer=arr
    
    return answer