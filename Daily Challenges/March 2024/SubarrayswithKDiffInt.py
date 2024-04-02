#Problem 992

from collections import defaultdict

def getting_the_count(nums, k):
    def subarrayWithKDistinct(k):

        counter = defaultdict(int)
        ans = left = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            ans += right - left + 1
        return ans
    return subarrayWithKDistinct(k) - subarrayWithKDistinct(k-1)

nums = [1,2,3,4,5,6,7]
k = 2
print(getting_the_count(nums, k))