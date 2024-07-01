#Problem 1550
#Solved on 1.7.24

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        if len(arr) < 3:
            return False
        
        for i in arr:
            if i % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        if count >= 3:
            return True
        else:
            return False

s = Solution()
nums = [1,2,34,3,4,5,7,23,12]
print(s.consecutiveOdds(nums))
        