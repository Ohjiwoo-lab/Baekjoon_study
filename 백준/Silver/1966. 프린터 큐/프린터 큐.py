# 실버 3 - 프린터 큐

from sys import stdin

t = int(stdin.readline().strip())
for i in range(t):
    cnt=1
    n, m = map(int, stdin.readline().strip().split())
    q = list(map(int, stdin.readline().strip().split()))
    q_list=[]
    for j in range(len(q)):
        q_list.append([q[j], j])

    while True:
        num,idx = q_list[0]
        del q_list[0]
        flag=True

        for a,b in q_list:
            if a > num:
                q_list.append([num,idx])
                flag=False
                break
        if flag:
            if idx==m:
                print(cnt)
                break
            else:
                cnt+=1