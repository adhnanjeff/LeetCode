#Problem 1530
#Solved in 18.7.24

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        def dfs(node) -> list[int]:
            if not node: return []
            if node.left is node.right:
                return [1]
            right = dfs(node.right)
            left = dfs(node.left)
            nonlocal res
            for r in right:
                for l in left:
                    if l + r <= distance:
                        res += 1
            leaves = []
            for x in right + left:
                x += 1
                if x < distance:
                    leaves.append(x)
            return leaves
        dfs(root)
        return res