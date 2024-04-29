#Problem 118

class Solution(object):
    def generate(self, numRows):
        l=[]
        if not numRows:
            return l
        l.append([1])
        for i in range(numRows-1):
            l.append([1,1])
        for i in range(2,numRows):
            for j in range(1,i):
                l[i].insert(j,(l[i-1][j-1]+l[i-1][j]))
        return l
    
s = Solution()
numRows = 5
ans = s.generate(numRows)
print(ans)