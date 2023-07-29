totalCost = int(input())
num = int(input())

sum = 0
for i in range(num):
    cost, n = map(int, input().split())
    sum += cost*n

if totalCost == sum:
    print("Yes")
else:
    print("No")