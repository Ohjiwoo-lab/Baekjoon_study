s = input()

sum = 0
for c in s:
    if c in ['A','B','C']:
        sum += 3
    elif c in ['D','E','F']:
        sum += 4
    elif c in ['G','H','I']:
        sum += 5
    elif c in ['J','K','L']:
        sum += 6
    elif c in ['M','N','O']:
        sum += 7
    elif c in ['P','Q','R','S']:
        sum += 8
    elif c in ['T','U','V']:
        sum += 9
    elif c in ['W','X','Y','Z']:
        sum += 10
    else:
        sum += 11

print(sum)