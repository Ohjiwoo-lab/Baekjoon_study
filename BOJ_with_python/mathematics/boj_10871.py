# X보다 작은 수

N, x = input().split()
N = int(N)
x = int(x)

A = []
for i in input().split():
    A.append(int(i))

for num in A:
    if num < x:
        print(num, end=" ")
