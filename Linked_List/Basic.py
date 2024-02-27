class Node:
    def __init__(self,data,address):
        self.data = data
        self.address = address


class Linked_List:
    def __init__(self):
        self.head = None
    
    def delete_at_begin(self):
        temp = self.head 
        self.head = self.head.address
        del temp

    def delete_at_end(self):
        if self.head.address == None:
            self.delete_at_begin()
        else:
            temp = self.head 
            while temp.address.address != None:
                temp = temp.address
            last_node = temp 
            last_node.address= None
            del temp

    def indert_at_begin(self,new_node):
        new_node.address = self.head
        self.head = new_node

    def indert_at_end(self,new_node):
        if self.head == None:
            self.indert_at_begin(new_node)
        else:
            temp = self.head
            while temp.address != None:
                temp = temp.address
            temp.address = new_node


    def traverse(self):
        temp = self.head
        while temp:
            print(f"{temp}: {temp.data} --> {temp.address}")
            temp = temp.address

    def create_temp_node(self):
        print("Enter Value of node")
        return Node(input(),None)

    def check_empty(self):
        if self.head == None:
            return True
        return False
    
    def convert_array_to_ll(self,arr):
        self.head = None
        for val in arr:
            node = Node(val,None)
            if self.head == None:
                self.head = node
            else:
                temp = self.head
                while temp.address != None:
                    temp = temp.address
                temp.address = node

    def remove_element_at_index(self,index_remove):
        temp = self.head
        index = 0

        if index == index_remove:
            self.delete_at_begin()
        else:
            while index+1 != index_remove and temp.address!= None:
                temp = temp.address
                index = index+1
            if temp.address== None:
                print("ERROR: Index out of range")
                return
            remove_node = temp.address
            temp.address = remove_node.address
            del remove_node

if __name__ == '__main__':
    ll = Linked_List()

    choice = 0
    while choice!=7:
        print("Menu:------")
        print("1: Insert at Begin:------")
        print("2: Insert at End:------")
        print("3: Delete Begin:------")
        print("4: Delete End:------")
        print("5: Create a Linked List from Array")
        print("6: Remove Element at Index")
        print("7: Exit")

        print("Please Enter Choice....")
        choice = int(input())
        if ll.check_empty() and choice not in (1,2,5,6):
            print("Empty Linked List")
            print("ERROR: Insert Element before Deleting....")
        else:
            if choice == 1:
                temp = ll.create_temp_node()
                ll.indert_at_begin(temp)
                ll.traverse()
            elif choice == 2:
                temp = ll.create_temp_node()
                ll.indert_at_end(temp)
                ll.traverse()
            elif choice == 3:
                ll.delete_at_begin()
                ll.traverse()
            elif choice == 4:
                ll.delete_at_end()
                ll.traverse()
            elif choice ==5 :
                print ("Enter count of elements to enter in array")
                count = int(input())
                arr = []
                for i in range(count):
                    print("enter Value")
                    arr.append(int(input()))
                ll.convert_array_to_ll(arr)
                ll.traverse()
            elif choice ==6:
                ll.traverse()
                print("Enter the index you want to remove from LL")
                index = int(input())
                ll.remove_element_at_index(index)
                ll.traverse()



    # node = Node(30,None)
    # ll.indert_at_begin(node)
    # node2 = Node(20,None)
    # ll.indert_at_begin(node2)
    # node2 = Node(10,None)
    # ll.indert_at_begin(node2)
    # ll.traverse()
    