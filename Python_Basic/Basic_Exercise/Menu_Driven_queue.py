from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self,element):
        self.queue.appendleft(element)
    
    def dequeue(self):
        if "Queue is Empty" == self.isempty():
            print("Queue is Empty no elements are present ",self.queue)
        else:
            self.queue.pop()
            print(self.queue)
    
    def display(self):
        print(self.queue)

    def isempty(self):
        if len(self.queue) ==0:
            return "Queue is Empty"
        else :
            return "Queue is not Empty"

if __name__ == '__main__':
    queue_var = Queue()

    choice = 0
    while choice!=5:
        print("Menu")
        print("1: Enqueue")
        print("2: Dequeue")
        print("3: Display")
        print("4: Check is empty")
        print("5: Exit")

        print("Enter choice")
        choice = int(input())
        if choice ==1:
            print("Enter element you want to insert")
            ele = input()
            queue_var.enqueue(ele)
        
        elif choice == 2:
            queue_var.dequeue()

        elif choice == 3:
            queue_var.display()

        elif choice == 4:
            print(queue_var.isempty())
