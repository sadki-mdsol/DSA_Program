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

    def removeNthFromEnd(self, head: Optional[ListNode], n1: int) -> Optional[ListNode]:
        # dummy = ListNode(0)
        # dummy.next = head
        # first = dummy
        # second = dummy

        # for _ in range(n + 1):
        #     first = first.next

        # while first is not None:
        #     first = first.next
        #     second = second.next

        # second.next = second.next.next

        # return dummy.next

        no_of_ele = 0
        temp = head
        while temp:
            no_of_ele +=1
            # print(f"{temp}: {temp.val} --> {temp.next}")
            temp = temp.next
        temp = head
        next_node = temp.next
        if no_of_ele == n1 :
            self.head = self.head.next
            return 
        no_of_ele -=1
        while no_of_ele != n1  and next_node.next != None and next_node is not None:
            no_of_ele -=1
            temp = next_node 
            next_node = next_node.next
        if no_of_ele == n1:
            temp.next = next_node.next
            next_node.next= None
            del next_node

        # if next_node.val != n1:
        #     print("Not Found")

l1 = ListNode(10)
l2 = ListNode(20)
l3 = ListNode(30)
l4 = ListNode(40)
l5 = ListNode(50)
s1 = Solution()

s1.insert_end(l1)
s1.insert_end(l2)
# s1.insert_end(l3)
# s1.insert_end(l4)
# s1.insert_end(l5)
s1.traverse()
print("After Deletion---------")

s1.removeNthFromEnd(s1.head,2)
s1.traverse()