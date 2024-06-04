#Problem 409
#Solved on 4.6.24

class Solution(object):
    def longestPalindrome(self, s):
        char_set = set()
        result = 0
        for char in s:
            if char in char_set:
                char_set.remove(char)
                result += 2
            else:
                char_set.add(char)
        if char_set:
            result += 1
        return result
        
s = Solution()
string = "abccccdd"
ans = s.longestPalindrome(string)
print(ans)