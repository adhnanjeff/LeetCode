#Problem 372

def superRow(a, b):
#Method 1
    """
    res = ""
    for i in b:
        res += str(i)

    return pow(a, int(res), 1337)
    """
#Method 2
    res = int("".join(map(str, b)))
    return pow(a, res, 1337)


a = 2147483647
b = [2, 0, 0]
ans = superRow(a, b)
print(ans)