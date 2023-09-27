def solution(survey, choices):
    answer = ''
    
    survey_dict = {
        "R":0, "T":0,
        "C":0, "F":0,
        "J":0, "M":0,
        "A":0, "N":0
    }
    
    for i, s in enumerate(survey):
        if choices[i]>4:
            survey_dict[s[1]]+=(choices[i]-4)
        else:
            survey_dict[s[0]]+=(4-choices[i])
    
    if survey_dict["R"]>=survey_dict["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if survey_dict["C"]>=survey_dict["F"]:
        answer += "C"
    else:
        answer += "F"
        
    if survey_dict["J"]>=survey_dict["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if survey_dict["A"]>=survey_dict["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer