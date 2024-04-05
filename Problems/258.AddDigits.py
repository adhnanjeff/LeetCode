def addDigits(num):
    def add(num):
        res = 0
        while num > 0:
            rem = num % 10
            res += rem
            num //= 10
        return res
    while num > 10:
        num = add(num)
    return num

num = 38
ans = addDigits(num)
print(ans)