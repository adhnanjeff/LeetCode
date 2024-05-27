#Problem 1608
#Solved on 27.5.24

class Solution(object):
    def specialArray(self, nums):
        nums.sort(reverse=True)
        n = len(nums)
        
        for i in range(n):
            if nums[i] >= i + 1 and (i == n - 1 or nums[i + 1] < i + 1):
                return i + 1
        
        return -1

s = Solution()
nums = [3,5]
ans = s.specialArray(nums)
print(ans)