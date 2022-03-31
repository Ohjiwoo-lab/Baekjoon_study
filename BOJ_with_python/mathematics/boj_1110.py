# 더하기 사이클

num = int(input())

count = 0
tens = num // 10
units = num % 10

while True:
    num_sum = tens + units
    tens = units
    units = num_sum % 10

    count += 1

    if (tens * 10 + units) == num:
        break

print(count)
