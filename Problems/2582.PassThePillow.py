#Problem 2582
#Solved on 6.7.24

class Solution:
    def passThePillow(self, n, time):
        chunks = time // (n - 1)
        return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))
    
s = Solution()
print(s.passThePillow(4, 5)) #Output: 2