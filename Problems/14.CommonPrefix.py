#Problem 14

def commonPrefix(str):
    n = len(str)
    i = 0 
    min_length = float('inf')
    for s in str:
        if len(s) < min_length:
            min_length = len(s)
    while i < min_length:
        for s in str:
            if s[i] != str[0][i]:
                return s[:i]
        i += 1
    return str[0][:i]


str = ["flower","flight", "florist","flu"]
ans = commonPrefix(str)
print(ans)