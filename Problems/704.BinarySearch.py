#Problem 704

def binarySearch(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid-1
        else:
            start = mid + 1
    return -1

nums = [5]
target = -5
ans = binarySearch(nums,target)
print(ans)