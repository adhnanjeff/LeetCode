#Problem 1614
#Solved on 4.4.24

def maxDepth(s):
    count = 0
    maxResult = 0
    for char in s:
        if char == "(":
            count += 1
            maxResult = max(maxResult, count)
        if char == ")":
            count -= 1
    return maxResult

s = "(1)+((2))+(((3)))"
ans = maxDepth(s)
print(ans)