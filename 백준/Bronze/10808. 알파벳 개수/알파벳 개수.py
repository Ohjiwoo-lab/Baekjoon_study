# 알파벳 개수

s = input()

ch_list = [0 for i in range(26)]
for ch in s:
      ch_list[ord(ch) - 97] += 1

for i in ch_list:
      print(i, end=" ")
