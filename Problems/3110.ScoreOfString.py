#Problem 3110
#Solved on 1.6.24

class Solution:
    def scoreOfString(self, s):
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score               
    
s = Solution()
print(s.scoreOfString("zaz"))