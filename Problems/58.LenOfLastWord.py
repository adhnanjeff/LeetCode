def lengthOfLastWord(s):
        l = 0
        new_s = s.strip()
        for i in range(len(new_s)):
            if new_s[i] == " ":
                l = 0
            else:
                l += 1
        return l

# Problem 58

s = "Hello World"
ans = lengthOfLastWord(s)
print(ans)