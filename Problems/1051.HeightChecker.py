#Problem 1051
#Solved on 10.6.24

class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        result = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result += 1
        return result 
        
s = Solution()
heights = [1,1,4,2,1,3]
ans = s.heightChecker(heights)
print(ans)
