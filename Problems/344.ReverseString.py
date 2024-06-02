#Problem 344
#Solved on 2.6.24

"s.reverse()" #Another method one liner 

class Solution(object):
    def reverseString(self, s):
        i = 0
        j = len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s
    
s = Solution()
print(s.reverseString(["h","e","l","l","o"]))