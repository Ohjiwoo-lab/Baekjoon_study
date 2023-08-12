n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))
    
num = 0
for i in range(n-1,-1,-1):
    if coin[i] > k:
        continue
    num += k//coin[i]
    k = k%coin[i]

print(num)