#Problem 1701
#Solved on 9.7.24

class Solution(object):
    def averageWaitingTime(self, customers):
        current_time = 0
        wait = 0
        for arrival, time in customers:
            if current_time < arrival:
                current_time = arrival
            wait += (current_time + time - arrival)
            current_time += time

        return float(wait) / len(customers)
    
s = Solution()
customers = [[1,2],[2,5],[4,3]]
print(s.averageWaitingTime(customers)) # Output: 5.0
