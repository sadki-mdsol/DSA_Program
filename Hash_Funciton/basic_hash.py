class HashTable:
    def __init__(self) -> None:
        self.my_arr = [None for i in range(0,200)]

    def get_hash(self,key):
        sum = 0
        for i in key:
            sum = sum+ord(i)
        return sum%100


    def set_value(self,key,value):
        index = self.get_hash(key)
        self.my_arr[index] = value

    def get_value(self,key):
        index = self.get_hash(key)
        return self.my_arr[index]
    
if __name__ == '__main__':
    ht = HashTable()

    choice = 0
    while choice != 3:
        print(ht.my_arr)
        print("Menu:-----")
        print("1 : Insert:-----")
        print("2 : Get:-----")
        print("3 : Exit:-----")

        print("Enter choice")
        choice = int(input())

        if choice == 1 :
            print("Enter Key")
            key = input()
            print("Enter Value")
            value = input()
            ht.set_value(key , value)
        if choice == 2 :
            print("Enter Key you want to get the value")
            key = input()
            print(ht.get_value(key))