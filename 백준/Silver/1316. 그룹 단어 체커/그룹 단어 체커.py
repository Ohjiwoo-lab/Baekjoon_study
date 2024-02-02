# 실버 5 - 그룹 단어 체커

from sys import stdin

n = int(stdin.readline())
answer = 0
for i in range(n):
    s = stdin.readline().strip()

    nDict = {}
    for j in range(len(s)):
        if nDict.get(s[j]) is None:
            nDict[s[j]]=j
        elif abs(nDict[s[j]]-j)<=1:
            nDict[s[j]]=j
        else:
            break
    else:
        answer += 1

print(answer)