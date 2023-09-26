num = []
max_nums = []
for i in range(9):
    n = list(map(int,input().split()))
    num.append(n)
    max_nums.append(max(n))

max_num = max(max_nums)
flag = False
for i in range(9):
    for j in range(9):
        if num[i][j]==max_num:
            print(max_num)
            print(i+1, j+1)
            flag = True
            break
    if flag:
        break