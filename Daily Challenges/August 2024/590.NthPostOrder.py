#Problem 590
#Solved on 26.8.24

class Solution(object):
    def postorder(self, root):
        if not root:
            return []

        res = []

        def dfs(root):
            for x in root.children:
                dfs(x)
            res.append(root.val)

        dfs(root)
        return res