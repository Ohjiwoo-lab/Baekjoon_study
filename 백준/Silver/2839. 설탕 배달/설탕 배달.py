from sys import stdin

n = int(stdin.readline())

if n < 5:
    if n%3 != 0:
        print(-1)
    else:
        print(n//3)
else:
    num = [0] * 2
    i = n//5
    while i >= 0:
        new_n = n - (5*i)
        if new_n % 3 == 0:
            num[0] = i
            num[1] = new_n//3
            break
        i-=1
    
    if num[0]+num[1] == 0:
        print(-1)
    else:
        print(num[0]+num[1])