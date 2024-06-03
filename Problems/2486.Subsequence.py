#Problem 2486
#Solved on 3.6.24

class Solution:
    def appendCharacters(self, s, t):
        i, j = 0, 0  
        
        while i < len(s) and j < len(t):  
            if s[i] == t[j]:  
                j += 1  
            i += 1 
        
        return len(t) - j 
               

s = Solution()
print(s.appendCharacters("coaching", "coding"))