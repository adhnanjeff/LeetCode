def missingNumber(nums):
    n = len(nums)
    return n*(n+1)/2 - sum(nums)

nums = [3,1,0]
ans = missingNumber(nums)
print(ans)