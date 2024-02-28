# Definition for singly-linked list.
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

    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        no_of_nodes = 0
        while temp.next!= None:
            temp = temp.next
            no_of_nodes = no_of_nodes+1
        
        temp = head
        result = 0
        while no_of_nodes >= 0:
            if int(temp.val) != 0:
                result = result+(2**no_of_nodes)
            no_of_nodes = no_of_nodes-1
            temp=temp.next
        print(no_of_nodes,result)


if __name__ == '__main__':
    s = Solution()
    v1 = s.create_temp_node()
    v2 = s.create_temp_node()
    v3 = s.create_temp_node()
    s.indert_at_end(v1)
    s.indert_at_end(v2)
    s.indert_at_end(v3)
    s.getDecimalValue(v1)
    # s.traverse()