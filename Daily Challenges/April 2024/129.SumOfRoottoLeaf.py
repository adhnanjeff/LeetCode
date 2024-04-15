#Problem 129
#Solved on 15.4.24

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        def dfs(node, path_sum):
            if not node:
                return 0
            path_sum = path_sum * 10 + node.val
            if not node.left and not node.right:
                return path_sum
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)

        return dfs(root, 0)
        