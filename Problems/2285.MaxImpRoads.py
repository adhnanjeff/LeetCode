#Problem 2285
#Solved on 28.6.24

class Solution:
    def maximumImportance(self, n, roads):
        res = 0
        cost = 1
        conn = [0] * n
        for road in roads:
            conn[road[0]] += 1
            conn[road[1]] += 1

        conn.sort()
        for con in conn:
            res += con * cost
            cost += 1
        return res
    
s = Solution()
print(s.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])) #43