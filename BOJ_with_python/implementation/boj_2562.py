# 최댓값

num_list = []
for i in range(9):
    num = int(input(''))
    num_list.append(num)

max_num = num_list[0]
max_seq = 0
for (i, n) in enumerate(num_list):
    if n > max_num:
        max_num = n
        max_seq = i
    else:
        continue

print(max_num)
print(max_seq+1)