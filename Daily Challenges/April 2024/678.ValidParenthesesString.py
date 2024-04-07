#Problem 678
#Solved on 7.4.24

def validParentheses(s):
    open_min = 0
    open_max = 0

    for i in s:
        if i == ")":
            open_min -= 1
            open_max -= 1
        elif i == "(":
            open_min += 1
            open_max += 1
        else:
            open_min -= 1
            open_max += 1

        if open_max < 0:
            return False
        open_min = max(0, open_min)

    return open_min == 0

s = "(((*))))"
ans = validParentheses(s)
print(ans) 