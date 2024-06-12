#Problem 75
#Solved on 12.6.24

class Solution(object):
    def sortColors(self, nums):
        s = m = 0
        l = len(nums)-1
        while m <= l:
            if nums[m] == 0:
                nums[s], nums[m] = nums[m], nums[s]
                s += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[l] = nums[l], nums[m]
                l -= 1
        return nums
        