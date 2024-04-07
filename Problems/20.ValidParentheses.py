#Problem 20

def validParentheses(s):
    stack = []

    if len(s) == 1:
        return False

    for char in s:
        if char in "({[":
            stack.append(char)

        elif char in ")}]":
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

    return len(stack) == 0

s = "){"
ans = validParentheses(s)
print(ans)
