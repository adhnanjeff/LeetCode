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

    def inorderTraversal(self, root, arr=None):
        if arr is None:
            arr = []
        if root:
            arr = self.inorderTraversal(root.left, arr)
            arr.append(root.data)
            arr = self.inorderTraversal(root.right, arr)
        return arr
    
    def preOrderTraversal(self, root, arr=None):
        if arr is None:
            arr = []
        if root:
            arr.append(root.data)
            arr = self.preorderTraversal(root.left, arr)
            arr = self.preorderTraversal(root.right, arr)
        return arr
    
if __name__ == "__main__":
    tree = BinaryTree()

    tree.insert(3)
    tree.insert(2)
    tree.insert(1)

    inorder_result = tree.inorderTraversal(tree.root)
    preorder_result = tree.preOrderTraversal(tree.root)
    print("Inorder Traversal:", inorder_result)
    print("PreOrderTraversal:", preorder_result)
