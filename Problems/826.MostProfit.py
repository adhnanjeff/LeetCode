#Problem 826
#Solved on 18.6.24

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        res, j, best, arr = 0, 0, 0, []
        
        for i in range(len(worker)):
            arr.append((difficulty[i], profit[i]))
        
        arr.sort()
        worker.sort()
        
        for work in worker:
            while j < len(arr) and work >= arr[j][0]:
                best = max(best, arr[j][1])
                j += 1
            
            res += best
        
        return res

s = Solution()
print(s.maxProfitAssignment([2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]))
        