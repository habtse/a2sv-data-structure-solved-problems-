# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        curr = head
        
        if head ==None or head.next==None:
            return head
        while curr: 
            curr = curr.next
            ls.append(curr)
        curr2 = head        
        # print(ls[-2].val)
        curr2.next = None
        for i in ls:
            if not i:
            
                break
            # print('current 322',curr2.val,curr2.next)

            i.next = curr2
            curr2 = i
            # print('current 322',curr2.val,curr2.next)
        # print(curr2)
        return curr2

            