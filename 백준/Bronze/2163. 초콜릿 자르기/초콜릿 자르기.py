# 브론즈 1 - 초콜릿 자르기

n,m = map(int, input().split())

if n>=m:
    print((m-1)+m*(n-1))
else:
    print((n-1)+n*(m-1))