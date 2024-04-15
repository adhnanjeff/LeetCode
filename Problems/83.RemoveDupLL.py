#Problem 83

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        pointer = head
        
        while pointer and pointer.next:
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head
        