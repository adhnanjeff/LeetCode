#Solved on 23.4.2024

class Solution(object):
    def reverse(self, head):
            pre_node = None
            current_node = head
            while current_node:
                next_node = current_node.next
                current_node.next = pre_node
                pre_node = current_node
                current_node = next_node
            return pre_node

    def reorderList(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)

        while rev.next is not None:
            temp = head.next
            revTemp = rev.next
            head.next = rev
            rev.next = temp
            head = temp
            rev = revTemp
        return head