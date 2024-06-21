#Problem 1052
#Solved on 21.6.24

class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)
        X = minutes
        satisfied = sum(customers[i] for i in range(n) if not grumpy[i])
        windowsum = sum(customers[i] for i in range(X) if grumpy[i])
        print(windowsum)
        maxsum = windowsum

        for r in range(X,n):
            windowsum += customers[r]*grumpy[r]
            windowsum -= customers[r-X]*grumpy[r-X]
            maxsum = max(maxsum, windowsum)
            
        return maxsum + satisfied
    
s = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

ans = s.maxSatisfied(customers, grumpy, minutes)
print(ans) #Expected: 16