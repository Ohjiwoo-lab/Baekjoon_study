# 실버 4 - 다항 함수의 미분

poly = input()
split_poly=poly.split('x')

if poly.find('x') == -1:
    print(0)
elif split_poly[0] == '':
    print(1)
elif split_poly[0] == '-':
    print(-1)
else:
    print(split_poly[0])