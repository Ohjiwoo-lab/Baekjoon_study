from sys import stdin

num = list(stdin.readline().strip())
num = list(map(int, num))

sum_num = 0
for n in num:
    sum_num += n**5

print(sum_num)