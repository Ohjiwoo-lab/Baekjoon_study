from sys import stdin

n=int(stdin.readline().strip())
num_list=list(map(int,stdin.readline().strip().split()))

num_set=list(set(num_list))
dict_num=[]
for i in range(n):
    dict_num.append([i,num_list[i]])

dict_num.sort(key=lambda x:x[1])

new_list=[0]*n
i=0
for j,num in enumerate(dict_num):
    if j!=0 and num[1]!=dict_num[j-1][1]:
        i+=1
    new_list[num[0]]=i

for i in new_list:
    print(i, end=" ")