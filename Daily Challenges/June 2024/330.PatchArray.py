#Problem 330
#Solved on 16.6.24

class Solution:
    def minPatches(self, nums, n):
        miss = 1
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                result += 1

        return result
    
s = Solution()
nums = [1, 3]
n = 6
print(s.minPatches(nums, n)) #Output: 1