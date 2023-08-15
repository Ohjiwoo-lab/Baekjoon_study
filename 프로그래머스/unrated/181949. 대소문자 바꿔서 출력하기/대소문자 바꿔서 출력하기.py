str = input()

trans_str = ""
for s in str:
    if s.islower():
        trans_str += s.upper()
    else:
        trans_str += s.lower()

print(trans_str)