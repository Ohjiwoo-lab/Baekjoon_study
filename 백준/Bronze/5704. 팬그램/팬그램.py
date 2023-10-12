while True:
    alpha=[0]*26
    
    s=input()
    if s=="*":
        break
    
    for i in s:
        if i.isalpha():
            alpha[ord(i)-97]+=1
    
    flag=True
    for i in alpha:
        if i==0:
            print("N")
            flag=False
            break
    if flag:
        print("Y")