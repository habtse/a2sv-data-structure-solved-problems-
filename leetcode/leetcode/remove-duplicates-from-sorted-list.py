# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        if not( head and head.next):
            return head
        curr1 = head.next
        curr2 =head
        visited.add(head.val)
        while curr1:
            if curr1.val in visited:
                if curr1.next:
                    curr2.next = curr1.next
                else:
                    curr2.next = None
                    return head
            else:
                visited.add(curr1.val)       
                curr2 =curr2.next
            curr1 = curr1.next

            
        return head
