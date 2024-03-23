x = -123
sum = 0
while x != 0:
    rem = x % 10
    sum = sum * 10 + rem
    x //= 10

print(sum)