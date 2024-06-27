#Problem 1791
#Solved on 27.6.24

class Solution(object):
    def findCenter(self, edges):
        a, b = edges[0]

        if edges[1][0] == a or edges[1][1] == a:
            return a
        else:
            return b

s = Solution()
edges = [[1,2],[2,3],[4,2]]
print(s.findCenter(edges))