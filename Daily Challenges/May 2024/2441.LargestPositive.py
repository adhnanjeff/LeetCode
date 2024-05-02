#Problem 2441
#SOLved on 3.5.24

class Solution(object):
    def findMaxK(self, nums):
        nums.sort()
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] > 0 and -nums[i] in nums:
                return nums[i]
        return -1
        

s = Solution()
nums = [-1, 2, -3, 3]
ans = s.findMaxK(nums)
print(ans) # Output: 2