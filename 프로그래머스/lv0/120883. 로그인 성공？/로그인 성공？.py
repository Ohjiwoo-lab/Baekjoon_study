def solution(id_pw, db):
    answer = ''
    
    flag = True
    for i in range(len(db)):
        if db[i][0] == id_pw[0]:
            if db[i][1] == id_pw[1]:
                answer = "login"
                flag=False
            else:
                answer = "wrong pw"
                flag=False

    if flag:
        answer="fail"
    
    return answer