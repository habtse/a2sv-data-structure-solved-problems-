# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        dummy1 = curr1 = ListNode()
        dummy2= curr2 = ListNode()

        while curr:
            count +=1
            if count % 2 ==0:
                curr2.next = curr
                curr2 = curr
            else:
                curr1.next = curr
                curr1 = curr
            
            curr= curr.next
        curr1.next = dummy2.next
        curr2.next = None
        return dummy1.next

        

        