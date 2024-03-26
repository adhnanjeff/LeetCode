#Solved on 25.4.2024

def findDuplicates(nums):
    dup = set()
    arr = set()
    for num in nums:
        if num in arr:
            dup.add(num)
        else:
            arr.add(num)

    return list(dup)

nums = [1,1,2]
ans = findDuplicates(nums)
print(ans)