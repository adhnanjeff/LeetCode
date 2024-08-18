#Problem 264
#Solved on 18.8.24

class Solution(object):
    def nthUglyNumber(self, n):
        primes = [2, 3, 5]
        next_ugly = [2, 3, 5]
        increase = [1, 1, 1]
        arr = [1]
        
        for _ in range(1, n):
            smallest = min(next_ugly)
            arr.append(smallest)
            
            for i in range(3):
                if next_ugly[i] == smallest:
                    increase[i] += 1
                    next_ugly[i] = primes[i] * arr[increase[i] - 1]
        
        return arr[-1]