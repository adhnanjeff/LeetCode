#Problem 1518
#Solved on 7.7.24

class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        return numBottles + (numBottles-1)//(numExchange-1)
    
s = Solution()
print(s.numWaterBottles(9, 3)) #Output: 13