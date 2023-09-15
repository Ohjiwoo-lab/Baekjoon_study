def solution(quiz):
    answer = []
    
    for i in quiz:
        x, op, y, eq, z = i.split()
        x=int(x)
        y=int(y)
        z=int(z)
        
        if op == '+' and x+y==z:
            answer.append("O")
        elif op == '-' and x-y==z:
            answer.append("O")
        else:
            answer.append("X")
    
    return answer