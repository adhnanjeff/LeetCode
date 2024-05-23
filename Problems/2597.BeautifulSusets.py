#Problem 2597
#Solved on 23.5.24

from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums, difference):
        tot_count = 1
        freq_map = defaultdict(dict)
        for num in nums:
            remainder = num % difference
            freq_map[remainder][num] = freq_map[remainder].get(num, 0) + 1

        for fr in freq_map.values():
            n = len(fr)
            curr_count = 1
            next1 = 1
            next2 = 0
            subsets = sorted(fr.items())
            for i in range(n - 1, -1, -1):
                skip = next1
                take = 2 ** subsets[i][1] - 1
                if i + 1 < n and subsets[i + 1][0] - subsets[i][0] == difference:
                    take *= next2
                else:
                    take *= next1
                curr_count = skip + take  
                next2, next1 = next1, curr_count

            tot_count *= curr_count

        return tot_count - 1
    
s = Solution()
nums = [1, 2, 4]
difference = 4
ans = s.beautifulSubsets(nums, difference)
print(ans)