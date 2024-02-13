# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ls =[]
        curr = head
        while curr:
            ls.append(curr.val)
            curr = curr.next
        total = 0
        n = len(ls)
        for i in range(n):
            n -=1
            total+=(ls[i]*(2**n))
            
        return total
