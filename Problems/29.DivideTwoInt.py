import math
class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 0
        
        ans = dividend/divisor
        if ans < 0:
             ans = math.ceil(ans)
        if ans > 0:
             ans = math.floor(ans)
        ans = int(ans)
        if ans < -2**31:
            return -2**31
        elif ans > 2**31-1:
            return 2**31-1
        else:
             return ans
        
sol = Solution()
ans = sol.divide(7, -3)
print(ans)



            
        