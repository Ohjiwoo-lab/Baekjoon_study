# 실버 3 - 크면서 작은 수

from sys import stdin
from itertools import permutations

x=stdin.readline().strip()
case=list(permutations(x,len(x)))

num=[]
for i in case:
    # 값을 만들 수 없는 경우 continue
    if i[0]=='0':
        continue
    s=''
    for j in i:
        s+=j

    # 기존 값과 같거나 작으면 continue
    if s<=x:
        continue
    # 기존 값보다 큰 경우만 값을 num에 넣는다.
    if s>x:
        num.append(s)

# num을 정렬해서 기존 값보다 큰 값들 중에 가장 작은 값을 출력
num.sort()

if len(num)==0:
    print(0)
else:
    print(num[0])