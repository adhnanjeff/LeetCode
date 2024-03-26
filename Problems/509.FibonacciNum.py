#Problem 509

def fib(n):
    nums = [0,1]
    if n == 0:
        return 0
    for i in range(2, n+1):
        nums.append(nums[i-1] + nums[i-2])
    return nums[-1]

n = 3
ans = fib(n)
print(ans)