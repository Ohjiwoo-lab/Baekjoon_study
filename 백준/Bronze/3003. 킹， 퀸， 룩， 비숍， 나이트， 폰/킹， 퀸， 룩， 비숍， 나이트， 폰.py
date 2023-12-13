# 브론즈 5 - 킹, 퀸, 룩, 비숍, 나이트, 폰

cnt = list(map(int, input().split()))

cntList=[1,1,2,2,2,8]
for i, n in enumerate(cnt):
    print(cntList[i]-n, end=" ")
