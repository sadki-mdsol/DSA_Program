from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        t1 = l1.head
        t2 = l2.head
        final_arr = []
        carrier = 0
        while t1 is not None or t2 is not None or carrier != 0 :
            if t1 is None:
                t1 = ListNode()
            if t2 is None:
                t2 = ListNode()
            sum = int(t1.val) + int(t2.val)
            final_arr.append((sum+carrier)%10)
            carrier = int((sum+carrier) / 10)
            if t1 is not None:
                t1 = t1.next
            if t2 is not None:
                t2 = t2.next
        # if carrier != 0 :
        #     final_arr.append(carrier)
        print(final_arr)


        print("returns an link list in form of Added value")
        t1 = l1.head
        t2 = l2.head
        dummyHead = ListNode(0)
        tail=dummyHead
        carrier = 0
        while t1 is not None or t2 is not None or carrier != 0:
            if t1 is None:
                t1 = ListNode()
            if t2 is None:
                t2 = ListNode()
            sum = int(t1.val) + int(t2.val)
            # final_arr.append((sum+carrier)%10)
            newNode=ListNode((sum+carrier)%10)
            tail.next=newNode
            tail = tail.next
            carrier = int((sum+carrier) / 10)
            if t1 is not None:
                t1 = t1.next
            if t2 is not None:
                t2 = t2.next
        # if carrier != 0 :
        #     newNode=ListNode((sum+carrier)%10)
        #     tail.next=newNode
        #     tail = tail.next

        result = dummyHead.next
        dummyHead.next = None
        return result
    
    def traverse(self):
        temp = self.head
        while temp:
            print(f"{temp}: {temp.val} --> {temp.next}")
            temp = temp.next

    def create_temp_node(self):
        print("Enter Value of node")
        return ListNode(input(),None)

    def indert_at_begin(self,new_node):
        new_node.next = self.head
        self.head = new_node

    def indert_at_end(self,new_node):
        if self.head == None:
            self.indert_at_begin(new_node)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

if __name__ == '__main__':
    s = Solution()
    v1 = s.create_temp_node()
    v2 = s.create_temp_node()
    v3 = s.create_temp_node()
    s.indert_at_end(v1)
    s.indert_at_end(v2)
    s.indert_at_end(v3)
    s.traverse()


    s1 = Solution()
    v1 = s.create_temp_node()
    v2 = s.create_temp_node()
    # v3 = s.create_temp_node()
    s1.indert_at_end(v1)
    s1.indert_at_end(v2)
    # s1.indert_at_end(v3)
    s1.traverse()

    final = s.addTwoNumbers(s,s1)
    temp = final
    while temp:
        print(f"{temp}: {temp.val} --> {temp.next}")
        temp = temp.next