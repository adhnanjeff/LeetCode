#Problem 861
#Solved on 13.5.24

class Solution:
    def matrixScore(self, grid):
        n, m= len(grid), len(grid[0])
        col1=[0]*m
        sum=0
        for row in grid:
            x=0
            one=False
            for i, b in enumerate(row):
                one=(row[0]==0)^(b==1)
                x=(x<<1)+one
                col1[i]+=one
            sum+=x
        for i in range(m):
            if col1[i]<=n//2:
                sum+=(1<<(m-1-i))*(n-2*col1[i])
        return sum
        
s = Solution()
grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
ans = s.matrixScore(grid)
print(ans)