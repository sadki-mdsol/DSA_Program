from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,element):
        self.container.append(element)

    def pop(self):
        if self.isempty() == "stack is not empty":
            self.container.pop()
        else:
            return "Stack is not having any elements"


    def isempty(self):
        return "Stack is empty" if len(self.container) ==0 else "stack is not empty"
    
    def getLength(self):
        return len(self.container)

    def getContainerEle(self):
        print(self.container)
    
    def peek(self):
        if self.isempty() == 'Stack is empty':
            return "Stack is Empty"
        else:
            return self.container[-1]

if __name__ =='__main__':
    stack = Stack()

    choice = 0
    while choice!=7:
        print("Menu")
        print("1: Push")
        print("2: Pop")
        print("3: Is Empty")
        print("4: Get Length")
        print("5: Display")
        print("6: Peek (display last element on stack)")
        print("7: Exit")

        print("Enter Choice")
        choice = int(input())

        if choice == 1:
            print("Enter element to push into stack")
            element = input()
            stack.push(element)
            
        elif choice == 2:
            print(stack.pop())
            print(stack.getContainerEle())
        
        elif choice == 3:
            print("Verify if stack is empty or not")
            print(stack.isempty())
        
        elif choice == 4:
            print("Length of the stack ")
            print(stack.getLength())
            
        elif choice == 5:
            print("Elements of stack are.....")
            print(stack.getContainerEle())
        
        elif choice == 6:
            print("Last Element of stack are.....")
            print(stack.peek())