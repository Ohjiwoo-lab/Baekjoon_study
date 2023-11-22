# 실버 5 - 너의 평점은

from sys import stdin

num_sum,score_sum=0.0,0.0
for i in range(20):
    major,num,score=stdin.readline().strip().split()
    if score=='P':
        continue

    num=float(num)
    num_sum+=num
    if score=='A+':
        score_sum+=(num*4.5)
    if score=='A0':
        score_sum+=(num*4.0)
    if score=='B+':
        score_sum+=(num*3.5)
    if score == 'B0':
        score_sum+=(num*3.0)
    if score == 'C+':
        score_sum+=(num*2.5)
    if score == 'C0':
        score_sum+=(num*2.0)
    if score == 'D+':
        score_sum+=(num*1.5)
    if score == 'D0':
        score_sum+=(num*1.0)
    if score == "F":
        continue

print(score_sum/num_sum)