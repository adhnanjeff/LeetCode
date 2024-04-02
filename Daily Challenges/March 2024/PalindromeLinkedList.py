#Date Solved: 22.03.2024

class Solution(object):
    
    def reverse(self, head):
        pre_node = None
        current_node = head

        while current_node != None:
            next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = next_node

        return pre_node

    def isPalindrome(self,head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)

        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True