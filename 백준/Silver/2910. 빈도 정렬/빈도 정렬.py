n,c=map(int,input().split())
num_list=list(map(int,input().split()))

num_dict={}
for i in num_list:
    if num_dict.get(i) is None:
        num_dict[i]=1
    else:
        num_dict[i]+=1

d=sorted(num_dict.items(),key=lambda x:x[1], reverse=True)
for num,cnt in d:
    for i in range(cnt):
        print(num, end=" ")