#Problem 287

def duplicate(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return num
        else:
            num_dict[num] = 1


nums = [1,2,3,4,5,]
ans = duplicate(nums)
print(ans)