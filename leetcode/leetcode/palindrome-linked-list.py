# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.before = []
        self.after = []
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        self.before.append(slow.val)
        fast = head 

        while fast.next and fast.next.next:
            slow = slow.next
            self.before.append(slow.val)
            fast = fast.next.next
        if fast.next:
            self.before.append('even')

        else:
            self.before.append('odd')
        leng = 0
        if self.before[-1] =='odd':
            leng = len(self.before)-3
        else:
            leng = len(self.before)-2
        slow =slow.next
        while slow:
            
            if slow.val != self.before[leng]:
                return False
            slow = slow.next
            leng -=1
        return True




        



        # self.middleNode(head)
        print(self.before)
        # print('reverseeas',reverse.val)
        # curr = head
        # print(head.next.next.val)
        # reverse = self.reverseList(head)
        # reversecurr = reverse
        # while curr :
        #     print (curr.val,reversecurr.val)
        #     if curr.val != reversecurr.val:
        #         return False
        #     reversecurr = reversecurr.next
        #     curr = curr.next
        #     print(curr)

        # return True
   