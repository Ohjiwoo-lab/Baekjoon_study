# 골드 4 - 좋은 친구

from sys import stdin

n, k = map(int, stdin.readline().strip().split())
name = []
for i in range(n):
    name.append(len(stdin.readline().strip()))

answer=0
name_dict={}
for i in range(1,k+1):
    if name_dict.get(name[i]) is None:
        name_dict[name[i]]=1
    else:
        name_dict[name[i]]+=1

for i in range(n-1):
    if name_dict.get(name[i]) is not None:
        answer+=name_dict[name[i]]

    name_dict[name[i+1]]-=1
    if i+k+1 <= n-1:
        if name_dict.get(name[i+k+1]) is None:
            name_dict[name[i+k+1]] = 1
        else:
            name_dict[name[i+k+1]] += 1

print(answer)