# 실버 5 - 부분 문자열

while True:
    try:
        s,t = input().split()
        j = 0
        for i in t:
            if j >= len(s):
                break
            if i == s[j]:
                j += 1

        if j == len(s):
            print("Yes")
        else:
            print("No")
    except:
        # 빈칸이 입력될 경우 break
        break