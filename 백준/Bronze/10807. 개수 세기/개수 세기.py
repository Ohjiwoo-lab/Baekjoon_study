n = int(input())
num_list = list(map(int, input().split()))
find_num = int(input())

count = 0
for num in num_list:
    if num == find_num:
        count += 1
        
print(count)