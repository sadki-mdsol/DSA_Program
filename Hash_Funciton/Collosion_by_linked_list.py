class HashTable:
    def __init__(self) -> None:
        self.my_arr = [[] for i in range(0,10)]

    def get_hash(self,key):
        sum = 0
        for i in key:
            sum = sum+ord(i)
        index =sum%10
        return index


    def __setitem__(self,key,value):
        index = self.get_hash(key)
        found = False
        for loc,ele in enumerate(self.my_arr[index]):
            if len(ele) == 2 and ele[0] == key:
                self.my_arr[index][loc] = (key,value)
                found = True
                break
        if not found:
            self.my_arr[index].append((key,value))
        
    def __getitem__(self,search_key):
        index = self.get_hash(search_key)
        for key,value in enumerate(self.my_arr[index]):
            if value[0] == search_key:
                return value[1]
            
    def delete_key(self,del_key):
        index = self.get_hash(del_key)
        for key,val in enumerate(self.my_arr[index]):
            if val[0] == del_key:
                del self.my_arr[index][key] #if we delete keyt then value will be removed tfrom the hash
        print(self.my_arr)
    
if __name__ == '__main__':
    ht = HashTable()
    # ht['march 6']=120
    # ht['march 6']=78
    # ht['march 8']=67
    # ht['march 9']=4
    # ht['march 17']=459

    # print(ht['march 6'])
    # print(ht['march 9'])

    choice = 0
    while choice != 5:
        print(ht.my_arr)
        print("Menu:-----")
        print("1 : Insert:-----")
        print("2 : Get:-----")
        print("3 : Update:-----")
        print("4 : Delete....")
        print("5 : Exit:-----")

        print("Enter choice")
        choice = int(input())

        if choice == 1 :
            print("Enter Key")
            key = input()
            print("Enter Value")
            value = input()
            ht[key]  = value # deafult mapped method __setitem__ will be invoked
            # ht.set_value(key , value) old method set_value will be invoked
        if choice == 2 :
            print("Enter Key you want to get the value")
            key = input()
            print(ht[key]) # deafult mapped method __getitem__ will be invoked
        if choice == 3 :
            print("Enter Key")
            key = input()
            print("Enter Value")
            value = input()
            ht[key]=value
        if choice == 4 :
            print("Enter Key")
            key = input()
            ht.delete_key(key)