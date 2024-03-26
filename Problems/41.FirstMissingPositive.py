#Problem 41

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