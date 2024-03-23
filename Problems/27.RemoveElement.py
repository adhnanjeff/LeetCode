#Problem 27
class Solution(object):
    def removeElement(self, nums, val):
        i = 0 
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
            else:
                i += 1
        return len(nums)
        