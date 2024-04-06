#Problem 1249
#Solved on 6.4.24

def minRemoveToMakeValid(s):
    stack = []
    uset = set()
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            if len(stack) == 0:
                uset.add(i)
            else:
                stack.pop()

    # Add remaining unmatched opening parentheses to the set
    while stack:
        uset.add(stack.pop())

    # Build the result string
    result = ""
    for i in range(len(s)):
        if i not in uset:
            result += s[i]

    return result



s = "lee(t(c)o)de)"
ans = minRemoveToMakeValid(s)
print(s)