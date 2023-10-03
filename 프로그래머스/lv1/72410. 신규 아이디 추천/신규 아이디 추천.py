def solution(new_id):
    answer = ''
    
    # 1단계
    one = new_id.lower()
    
    # 2단계
    two=''
    for i in one:
        if i.isalpha() or i.isdigit() or i=="_" or i=="." or i=="-":
            two+=i
    
    # 3단계
    flag,three=False,''
    for i in two:
        if i==".":
            if not flag:
                flag=True
                three+="."
        else:
            flag=False
            three+=i
            
    # 4단계
    four=''
    if three[0]=="." and three[-1]==".":
        four=three[1:-1]
    elif three[0]==".":
        four=three[1:]
    elif three[-1]==".":
        four=three[:-1]
    else:
        four=three
        
    # 5단계
    if len(four)==0:
        four='a'
    
    # 6단계
    if len(four)>=16:
        four=four[:15]
        if four[-1]==".":
            four=four[:-1]
    
    # 7단계
    if len(four)<=2:
        num=four[-1]
        print(num)
        for _ in range(3-len(four)):
            four+=num
    
    answer=four
    
    return answer