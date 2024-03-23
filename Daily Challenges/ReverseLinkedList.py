#Date Solved: 21.03.2024

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        pre_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = next_node

        return pre_node