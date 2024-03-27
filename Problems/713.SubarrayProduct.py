def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
            return 0

    product = 1
    count = 0
    left = 0

    for right, num in enumerate(nums):
        product *= num
        while product >= k:
            product /= nums[left]
            left += 1
        count += right - left + 1

    return count

nums = [1,1,1]
k = 100
ans = numSubarrayProductLessThanK(nums, k)
print(ans)