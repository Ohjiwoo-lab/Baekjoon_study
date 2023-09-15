#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    num_list = list(map(int, input().split()))
    max_index,min_index = 0,0
    
    for i in range(1,n):
        if num_list[i] >= num_list[max_index]:
            max_index=i
        if num_list[i] < num_list[min_index]:
            min_index=i
    print(f"#{test_case} {abs(max_index-min_index)}")
