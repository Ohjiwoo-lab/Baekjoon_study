# 브론즈 2 - 단어순서 뒤집기

n=int(input())
for i in range(n):
    s=list(input().split())
    s.reverse()

    print(f"Case #{i+1}: ",end="")
    for j in s:
        print(j,end=" ")
    print()