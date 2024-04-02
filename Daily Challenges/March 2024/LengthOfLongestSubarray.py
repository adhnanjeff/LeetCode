#Solved on 28.04.2024

def maxSubarrayLength(nums, k):
    n = len(nums)
    i = j = result = 0
    dict_data = {}

    while j < n:
        dict_data[nums[j]] = dict_data.get(nums[j],0) + 1 
        while i < j and dict_data[nums[j]] > k:
            dict_data[nums[i]] -= 1  
            i += 1
        result = max(result, j - i + 1)
        j += 1
    return result

nums = [1, 2, 3, 1, 2, 3, 1, 2]
ans = maxSubarrayLength(nums, 2)
print(ans)
