#Problem 1514
#Solved on 5.4.24

def makeGood(s):
    stack = []
    for char in s:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

s = "leEeetcode"
ans = makeGood(s)
print(ans)