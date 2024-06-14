#Problem 945
#Solved on 14.6.24

class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()  
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                count += increment
        
        return count

s = Solution()
print(s.minIncrementForUnique([1,2,2]))
