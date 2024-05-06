#Problem 237
#Solved on 5.5.24

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next