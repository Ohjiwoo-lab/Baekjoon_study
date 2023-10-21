# 실버 5 - 팬그램

n=int(input())
for i in range(n):
    alpha=[0]*26
    s=input()
    for j in s:
        if j.isalpha():
            alpha[ord(j.lower())-97]+=1

    print(f"Case {i+1}: ", end="")
    if 0 in alpha:
        print("Not a pangram")
    elif 1 in alpha:
        print("Pangram!")
    elif 2 in alpha:
        print("Double pangram!!")
    else:
        print("Triple pangram!!!")