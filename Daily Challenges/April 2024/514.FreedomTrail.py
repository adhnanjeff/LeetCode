#Problem 514
# 27.4.24

from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring, key):
        n, m = len(ring), len(key)
        dp = [[float('inf')] * n for _ in range(m)]
        pos = [[] for _ in range(26)]
        for i in range(n):
            pos[ord(ring[i]) - ord('a')].append(i)
        for i in pos[ord(key[0]) - ord('a')]:
            dp[0][i] = min(i, n - i) + 1
        for i in range(1, m):
            for j in pos[ord(key[i]) - ord('a')]:
                for k in pos[ord(key[i - 1]) - ord('a')]:
                    diff = abs(j - k)
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(diff, n - diff) + 1)
        return min(dp[m - 1])
    
s = Solution()
ring = "godding"
key = "gd"
ans = s.findRotateSteps(ring, key)
print(ans)