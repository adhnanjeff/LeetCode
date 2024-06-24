#Problem 995
#Solved on 24.6.24

class Solution(object):
    def minKBitFlips(self, nums, k):
        n = len(nums)
        flip = [0] * n
        current_flips = 0
        result = 0

        for i in range(n):
            if i >= k:
                current_flips ^= flip[i - k]
            
            if (nums[i] ^ current_flips) == 0:
                if i + k > n:
                    return -1
                result += 1
                current_flips ^= 1
                if i + k < n:
                    flip[i] = 1
        
        return result 
    
s = Solution()
nums = [1, 0, 1]
k = 1
print(s.minKBitFlips(nums, k)) #Output: 2
