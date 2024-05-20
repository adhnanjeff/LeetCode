#Problem 1863
#Solved on 20.5.24

class Solution:
    def subsetXORSum(self, nums):
        result = 0
        subsets = [0]
        for n in nums:
            new_subsets = list(subsets)
            for s in subsets:
                new_subsets.append(s ^ n)
                result += new_subsets[-1]
            subsets = new_subsets    
        return result
    
s = Solution()
nums = [1,3]
ans = s.subsetXORSum(nums)