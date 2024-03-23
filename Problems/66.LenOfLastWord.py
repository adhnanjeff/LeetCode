#Problem 66

def lengthOfLastWord(s):
    sum = ""
    for i in range(0, len(s)):
        sum += str(s[i])
    sum = int(sum) + 1
    res = []
    res.append(sum)
    
    split_arr = [int(char) for char in str(res[0])]
    return split_arr

s = [9,9]
ans = lengthOfLastWord(s)
print(ans)
