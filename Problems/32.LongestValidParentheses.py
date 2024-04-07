#Problem 32
def longestValidParentheses(self, s):
        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length

s = "(()"
ans = longestValidParentheses(s)
print(ans)

#Intuition
"""
def longestValidParentheses(s):
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
    while stack:
        uset.add(stack.pop())

    res = ""
    for i in range(len(s)):
        if i not in uset:
            res += s[i]
    return len(res)
"""
