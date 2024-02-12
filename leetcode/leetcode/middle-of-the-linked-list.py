# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head 
        if slow.next == None:
            return head
        if slow.next.next ==None:
            return slow.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            return slow.next
        else:
            return slow