#Solved on 26.04.2024

def firstMissingPositive(nums):
    nums_set = set(nums)

    if 1 not in nums_set:
        return 1

    i = 2
    while i in nums_set:
        i += 1

    return i

nums = [1,2,10,9]
ans = firstMissingPositive(nums)
print(ans)

"""
    def firstMissingPositive(nums):
    nums_array = sorted(set(nums))
    start = nums[0]
    end = nums[len(nums)-1]
    arr = []

    if start > 1 or start < 0:
        return 1

    for i in range(start, end+1):
        if i > 0:
            arr.append(i)
    for num in arr:
        if num not in nums_array and num > 0:
            return num
        
    return end+1
        
"""



