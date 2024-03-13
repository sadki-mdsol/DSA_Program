from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def __init__(self) -> None:
        self.head = None

    def insert_end(self,node):
        temp = self.head
        if self.head == None:
            self.head=node
        else:
            while temp.next != None:
                temp= temp.next
            temp.next = node

    def traverse(self):
        temp = self.head
        while temp:
            print(f"{temp}: {temp.val} --> {temp.next}")
            temp = temp.next

    def removeNthFromEnd(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None :
            return None
        temp = head
        next_node = temp.next
        while next_node!= None:
            if temp.val == val:
                self.head = self.head.next
                temp = self.head
                # next_node = temp.next
            elif next_node.val != val:
                temp = temp.next
            else:
                temp.next = next_node.next
                # next_node = next_node.next
            next_node = temp.next
        if temp.val == val:
            self.head = None

[1,2,6,3,4,5,6]

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
s1 = Solution()


s1.insert_end(l1)
s1.insert_end(l2)
s1.insert_end(l3)
s1.insert_end(l4)
s1.insert_end(l5)
s1.insert_end(l6)
s1.traverse()
print("After Deletion---------")

s1.removeNthFromEnd(s1.head,6)
s1.traverse()