def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    n = len(A)
    for i in range(n):
        num1 = A.pop()
        num2 = B.pop()
        answer += num1 * num2

    return answer