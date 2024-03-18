# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        common_set= set()
        currA = headA
        currB = headB
        while currA or currB:
            if currA in common_set:
                return currA
            if currA:
                common_set.add(currA)
                currA = currA.next

                
            if currB in common_set:
                return currB
            if currB:
                common_set.add(currB)
                currB = currB.next
            
            
        return None
        

        