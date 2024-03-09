# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        f = head
        while f and f.next and f.next.next:
            s = s.next
            f = f.next.next
            if s == f:
                break
        if head and head.next and head.next.next and s != f:
            return None
        elif not head or not head.next or not head.next.next:
            return None             
        else:
            f = head
            while s != f:
                s = s.next
                f = f.next
            return f

       