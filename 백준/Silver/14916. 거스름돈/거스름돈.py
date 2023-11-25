# 실버 5 - 거스름돈

n=int(input())

answer=-1
five=n//5
for i in range(five,-1,-1):
    tmp=n-i*5
    if tmp%2 == 0:
        answer=i+(tmp//2)
        break

print(answer)