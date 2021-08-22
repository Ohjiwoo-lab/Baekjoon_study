# 직사각형에서 탈출

x, y, w, h = input('').split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

min_value = min(x, y, (h - y), (w - x))  # 4가지 경우 중 가장 짧은 거리

print(min_value)