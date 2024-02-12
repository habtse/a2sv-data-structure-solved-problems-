# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using dictionary
        # visted = {}
        # curr = head
        # if curr == None or curr.next == None:
        #     return False
        # while curr.next:
        #     if curr.next in visted:
        #         return True
        #     visted[curr.next] = 1
        #     curr = curr.next
        # return False
        fast =head
        slow = head
       
        while  fast and fast.next:
            if fast.next.next ==slow.next:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
