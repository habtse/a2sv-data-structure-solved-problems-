class Node:
    def __init__ (self,val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index):
            if not curr:
                return -1
            curr = curr.next
        return curr.val if curr else -1
    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            curr = Node(val)
            curr.next = self.head
            self.head = curr
            # temp = self.head
            # self.head = Node(val)
            # self.head.next = temp
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head=Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index-1):
                if not curr:
                    return
                curr = curr.next
            if curr:
                temp = Node(val)
                temp.next = curr.next
                curr.next = temp
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            curr = self.head
            for i in range(index-1):
                if not curr:
                    return
                curr= curr.next
            if curr and curr.next:
                curr.next = curr.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)