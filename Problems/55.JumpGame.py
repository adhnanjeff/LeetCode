def canJump(nums):
    
    last = len(nums) - 1
    print(last)
    i = 0

    if len(nums) == 1:
        return True

    while i < len(nums):
        if nums[i] == 0:
            return False
        i += nums[i] 
        
        if i == last:
            return True
        
    return False

nums = [1,2]
ans = canJump(nums)
print(ans)