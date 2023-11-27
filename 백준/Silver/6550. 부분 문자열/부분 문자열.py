# 실버 5 - 부분 문자열

from sys import stdin

while True:
    st = stdin.readline().strip()
    # 빈칸이 입력될 경우 break
    if not st:
        break
    s,t=st.split()
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