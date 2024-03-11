# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # total_count = len(head)
        dummy = slow = ListNode()
        # dummy.next = head
        fast = head
        slow.next = head
        count = 1
        # curr = dummy
        # required = dummy
        while fast: 
            # curr = curr.next
            # fast +=1
            if count > n:
                slow = slow.next
            fast = fast.next
            count += 1
        slow.next = slow.next.next       
        
        return dummy.next
                

                
        

            
        