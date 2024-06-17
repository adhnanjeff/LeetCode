#Problem 633
#Solved on 17.6.24

import math
class Solution(object):
    def judgeSquareSum(self, c):
        l = 0
        r = int(math.sqrt(c))

        while l <= r:
            sum = l * l + r * r
            if sum == c:
                return True
            elif sum < c:
                l += 1
            else:
                r -= 1
        return False 
        

s = Solution()
print(s.judgeSquareSum(5))
