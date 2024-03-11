# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        fast = head
        dummy = slow= ListNode()
        count = 1
        ls = []
        while count <= right:
            
            if count >= left :
                ls.append(fast.val)
            else: 
                slow.next = ListNode(fast.val)  
                slow = slow.next      
            count += 1
            fast = fast.next
        print(dummy)
        for i in range(len(ls)-1, -1, -1):
            while i == len(ls)-1 and slow.next:
                slow = slow.next
            
            slow.next = ListNode(ls[i])
            slow = slow.next
        
        slow.next = fast

        return dummy.next
        

