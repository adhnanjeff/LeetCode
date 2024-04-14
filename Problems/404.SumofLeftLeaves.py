#Problem 404

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def solve(self, curr, par):
        if curr == None:
            return 0
        if curr.left == None and curr.right == None:
            if par is not None and par.left == curr:
                return curr.val

        right = self.solve(curr.right, curr)
        left = self.solve(curr.left, curr)
        return left + right
    
    def sumOfLeftLeaves(self, root):
        return self.solve(root, None)
        