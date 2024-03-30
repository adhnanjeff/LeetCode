def countSubarrays(nums,k):
    result = 0
    maxE = max(nums)
    maxE_count = 0
    n = len(nums)
    j = 0

    """ Use for loop instead of while loop
    to avoid infinite looping """

    for i in range(n):
        if nums[i] == maxE:
            maxE_count += 1
        if maxE_count < k:
            continue
        while maxE_count >= k:
            result += n - i
            if nums[j] == maxE:
                maxE_count -= 1
            j += 1
    return result

nums = [1,3,2,3,3]
ans = countSubarrays(nums,2)
print(ans)