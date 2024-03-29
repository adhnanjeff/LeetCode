#Problem 75
"""Dutch National Flag Algorithm"""

def  sortColors(nums):
    start = mid = 0
    last = len(nums) - 1

    while mid <= last:
        if nums[mid] == 0:
            nums[start], nums[mid] = nums[mid], nums[start]
            start += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[last] = nums[last], nums[mid]
            last -= 1
    return nums

nums = [2,0,2,1,1,0]
ans = sortColors(nums)
print(ans)