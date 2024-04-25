#Problem 2370
#Solved on 25.4.24

class Solution:
    def longestIdealString(self, s, k):
        n = len(s)
        dp = [0]*26
        dp[ord(s[0])-97] += 1

        for i in range(1, n):
            ordi = ord(s[i]) - 97
            dp[ordi] = 1 + max(dp[max(0, ordi-k):min(26, ordi+k+1)])
        
        return max(dp)
    
sol = Solution()
input_str = 'abcdfg'  
k = 2
ans = sol.longestIdealString(input_str, k) 
print(ans)




