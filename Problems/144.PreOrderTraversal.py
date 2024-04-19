#Problem 144

"Change the nodes value to val instead of data"

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(data, self.root)

    def _insert_recursively(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert_recursively(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert_recursively(data, current_node.right)
    
    def preorderTraversal(self, root, arr=None):
        if arr is None:
            arr = []
        if root:
            arr.append(root.data)
            arr = self.preorderTraversal(root.left, arr)
            arr = self.preorderTraversal(root.right, arr)
        return arr
    
    def postorderTraversal(self, root, arr=None):
        if arr is None: 
            arr = [] 
        if root:
            arr = self.postorderTraversal(root.left, arr)
            arr = self.postorderTraversal(root.right, arr)
            arr.append(root.data)  
        return arr
    
if __name__ == "__main__":
    tree = BinaryTree()

    tree.insert(3)
    tree.insert(2)
    tree.insert(1)

    preorder_result = tree.preorderTraversal(tree.root)
    postorder_result = tree.postorderTraversal(tree.root)
    print("PreOrderTraversal:", preorder_result)
    print("PostOrderTraversal:", postorder_result)
