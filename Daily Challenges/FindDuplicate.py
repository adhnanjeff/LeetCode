#Solved on 24.4.2024

"""def duplicate(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return num
        else:
            num_dict[num] = 1


nums = [1,2,3,4,5,]
ans = duplicate(nums)
print(ans)"""

"""  def find_duplicate(nums):
    # Phase 1: Detect if there's a cycle
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Phase 2: Find the start of the cycle
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    
    return ptr1

nums = [1, 2, 3, 4, 2]
ans = find_duplicate(nums)
print(ans)      """

def duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
    
nums = [1,2,3,4,2]
ans = duplicate(nums)
print(ans)