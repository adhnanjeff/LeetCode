#Problem 1509
#Solved on 3.7.24

class Solution:
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0

        nums.sort()
        ans = nums[-1] - nums[0]
        
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i])
        return ans

s = Solution()
print(s.minDifference([5, 3, 2, 4])) # Output: 0