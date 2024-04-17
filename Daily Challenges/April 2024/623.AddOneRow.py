#Problem 623
#Solved on 16.4.24

def add(self,root, val, depth, curr):
    if not root:
        return root
    
    if curr == depth - 1:
        lTemp = root.left
        rTemp = root.right

        root.left = TreeNode(val)
        root.right = TreeNode(val)
        root.left.left = lTemp
        root.right.right = rTemp

        return root
    
    root.left = self.add(root.left, val, depth)
    root.right = self.add(root.right, val, depth)

    return root

def addOneRow(self, root, val, depth):
    if depth == 1:
        newRoot = TreeNode(val)
        newRoot.left = root
        return newRoot
    
    return self.add(root, val, depth, 1)