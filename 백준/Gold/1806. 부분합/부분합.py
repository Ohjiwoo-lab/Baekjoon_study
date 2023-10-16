from sys import stdin

n, m = map(int, stdin.readline().strip().split())
num = list(map(int, stdin.readline().strip().split()))

inf = float('inf')
answer = inf

num_sum = 0
s, e = 0, -1
while True:
    if m == 0:
        answer = 1
        break

    if answer == 1:
        break

    if num_sum > m:
        if answer > (e - s + 1):
            answer = e - s + 1
        num_sum -= num[s]
        s += 1
        if s > e:
            s = e
            e -= 1
            num_sum = 0
    elif num_sum == m:
        if answer > (e - s + 1):
            answer = e - s + 1
        if e+1 >= n:
            break
        e = s
        s += 1
        num_sum = 0
    else:
        e += 1
        if e >= n:
            break
        num_sum += num[e]

if answer == inf:
    print(0)
else:
    print(answer)