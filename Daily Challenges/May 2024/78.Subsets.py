#Problem 78
#Solved on 21.5.24

class Solution:
    def subsets(self, nums):
        def backtrack(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        result = []
        backtrack(0, [])
        return result
    
s = Solution()
nums = [1,2,3]
ans = s.subsets(nums)
print(ans)