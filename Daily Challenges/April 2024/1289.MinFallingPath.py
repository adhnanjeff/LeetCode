#Problem 1289
#Solved 26.4.2024

class Solution:
    def minFallingPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])
        tmp = []
        cprev=-1
        for r in range(row):
            if r>0:
                tmp=sorted(grid[r-1])
                for c in range(col):
                    if grid[r-1][c] == tmp[0]:
                        grid[r][c] += tmp[1]
                    else:
                        grid[r][c] += tmp[0]
                    
        
        return min(grid[row-1])
    
s = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]

ans = s.minFallingPathSum(grid) 
print(ans)