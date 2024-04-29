#Problem 2997
#Solved on 29.4.24

class Solution:
    def minOperations(self, nums, k):
        xor = nums[0]
        for a in nums[1:]:
            xor ^= a
        xor = str(bin(xor))[2:]
        k = str(bin(k))[2:]
        if len(xor) > len(k):
            k = k.rjust(len(xor), "0")
        else:
            xor = xor.rjust(len(k), "0")
        ans = 0
        for b1, b2 in zip(xor, k):
            ans += b1 != b2
        return ans
    
s = Solution()
nums = [2, 1, 3, 4]
k = 1
ans = s.minOperations(nums, k)
print(ans)