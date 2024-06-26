#Problem 1382
#Solved on 26.6.24

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root):
        # Perform inorder traversal and get sorted array of nodes
        sorted_nodes = self.inorderTraverse(root)
        # Build and return balanced BST from sorted array
        return self.sortedArrayToBST(sorted_nodes, 0, len(sorted_nodes) - 1)

    def inorderTraverse(self, root):
        sortedArr = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            sortedArr.append(current)
            current = current.right
        return sortedArr

    def sortedArrayToBST(self, sortedArr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = sortedArr[mid]
        root.left = self.sortedArrayToBST(sortedArr, start, mid - 1)
        root.right = self.sortedArrayToBST(sortedArr, mid + 1, end)
        return root
    

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)


solution = Solution()
balanced_root = solution.balanceBST(root)

def inorder_print(node):
    if node:
        inorder_print(node.left)
        print(node.val, end=' ')
        inorder_print(node.right)

inorder_print(balanced_root)  # Output: 2 1 3 4