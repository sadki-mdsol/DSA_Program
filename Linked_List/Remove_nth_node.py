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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        next_node = temp.next

        while next_node.next != None and next_node.val != n :
            temp = next_node 
            next_node = next_node.next

        if next_node.val == n:
            temp.next = next_node.next
            next_node.next= None
            del next_node

        if next_node.val != n:
            print("Not Found")

l1 = ListNode(10)
l2 = ListNode(20)
l3 = ListNode(30)
l4 = ListNode(40)
l5 = ListNode(50)
s1 = Solution()

s1.insert_end(l1)
s1.insert_end(l2)
s1.insert_end(l3)
s1.insert_end(l4)
s1.insert_end(l5)
s1.traverse()
print("After Deletion---------")

s1.removeNthFromEnd(s1.head,100)
s1.traverse()