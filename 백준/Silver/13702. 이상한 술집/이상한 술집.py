# 실버 3 - 이상한 술집

from sys import stdin

# 입력 받기
n,k=map(int,stdin.readline().strip().split())
cap=[]
for i in range(n):
    cap.append(int(stdin.readline()))

answer=0
m=max(cap)

# 주전자의 개수가 1일 때 (예외 처리)
if n==1:
    answer=cap[0]//k
# 주전자가 1개보다 많은 경우 (이분탐색)
else:
    left,right=0,m
    while left <= right:
        mid=(left+right)//2

        # 만약 mid가 0인 경우 (예외 처리) - mid로 나누기 연산을 하므로
        if mid==0:
            answer=mid
            left=mid+1
            continue

        # mid가 0이 아닌 경우에만 현재 mid로 몇 명한테 줄 수 있는지 검사
        s=0
        for c in cap:
            s+=(c//mid)

        # 줄 수 있는 사람 수가 k보다 많거나 같으면?
        # mid 용량을 더 늘려서 최대값을 찾아야 함.
        if s>=k:
            answer=mid
            left=mid+1
        # 작으면, mid 용량을 줄여서 사람 수를 늘려야 함.
        else:
            right=mid-1
print(answer)