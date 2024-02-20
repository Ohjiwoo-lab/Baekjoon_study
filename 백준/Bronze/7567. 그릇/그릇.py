s = input()

b = s[0]
answer = 10
for i in range(1, len(s)):
    if s[i]==b:
        answer += 5
    else:
        answer += 10
        b = s[i]

print(answer)