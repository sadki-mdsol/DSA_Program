# Definition for singly-linked list.

import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.head = None

    def indert_at_end(self,new_node):
        if self.head == None:
            self.indert_at_begin(new_node)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
    
    def create_temp_node(self):
        print("Enter Value of node")
        return ListNode(input(),None)

    def indert_at_begin(self,new_node):
        new_node.next = self.head
        self.head = new_node

    def getMiddleList(self, head: ListNode) -> int:
        temp = head
        no_of_nodes = 1
        while temp.next!= None:
            temp = temp.next
            no_of_nodes = no_of_nodes + 1
        
        total_node_count= no_of_nodes
        dummy_head = ListNode()
        temp_result = dummy_head
        temp = head
        while temp!= None:
            if no_of_nodes <= ((total_node_count/2)+(total_node_count%2)):
                copy = ListNode(temp.val)
                temp_result.next=copy
                temp_result = temp_result.next
            temp=temp.next
            no_of_nodes = no_of_nodes-1
            
            
        
        result = dummy_head.next
        dummy_head.next = None
        print(total_node_count)
        return result


if __name__ == '__main__':
    s = Solution()
    v1 = s.create_temp_node()
    v2 = s.create_temp_node()
    v3 = s.create_temp_node()
    v4 = s.create_temp_node()
    v5 = s.create_temp_node()
    # v6 = s.create_temp_node()
    s.indert_at_end(v1)
    s.indert_at_end(v2)
    s.indert_at_end(v3)
    s.indert_at_end(v4)
    s.indert_at_end(v5)
    # s.indert_at_end(v6)
    final = s.getMiddleList(v1)
    temp = final
    while temp:
        print(f"{temp}: {temp.val} --> {temp.next}")
        temp = temp.next
    # s.traverse()