#Problem 979
#Solved on 18.5.24

class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            
            L = dfs(node.left)
            R = dfs(node.right)
            self.ans += abs(L) + abs(R)
            
            return node.val + L + R - 1
        
        dfs(root)
        
        return self.ans
    
s = Solution()
print(s.distributeCoins([3,0,0]))