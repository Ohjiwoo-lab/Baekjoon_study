# 브론즈 2 - 5와 6의 차이

a, b = input().split()

maxA, maxB = '',''
minA, minB = '',''

for i in a:
    if i=='5':
        maxA+='6'
    else:
        maxA+=i

for i in b:
    if i=='5':
        maxB+='6'
    else:
        maxB+=i

for i in a:
    if i=='6':
        minA+='5'
    else:
        minA+=i

for i in b:
    if i=='6':
        minB+='5'
    else:
        minB+=i

print(int(minA)+int(minB), int(maxA)+int(maxB))