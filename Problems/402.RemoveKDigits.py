#Problem 402


def removeKdigits(num, k):
    stack = []

    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    stack = stack[:-k] if k > 0 else stack
    result = ''.join(stack).lstrip('0')

    return result if result else '0'

num = "1432219"
k = 3
ans = removeKdigits(num, k)
print(ans)