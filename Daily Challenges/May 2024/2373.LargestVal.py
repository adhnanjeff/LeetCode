#Problem 2373
#Solved on 12.5.24

class Solution(object):
    def largestLocal(self, grid):
        arr = [[0]* (len(grid) - 2) for _ in range(len(grid) - 2)]
        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] = max(max(grid[i][j:j+3]),  max(grid[i+1][j:j+3]), max(grid[i+2][j:j+3]))
        return arr