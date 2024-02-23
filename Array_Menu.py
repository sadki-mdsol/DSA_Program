# "********** Menu Driven Program Array *****************"
# "Menu"
# "1: Display"
# "2: Insertion"
# "3: Deletion"
# "4: Search"
# "5: Update"
# "6: Exit"

def display_elements(elements):
    print("The Elements Are:....")
    for ele in elements:
        print(ele)

def insert_element(arr_main):
    print ("Enter element you want to insert")
    arr_main.append(int(input()))

def delete_element(arr_main):
    arr_main.remove()

def search_element(arr_main):
    print(arr_main)
    print("Enter element you want to search")
    search = int(input())
    for val in arr_main:
        if val is search:
            return f"Search value {search} is found in {arr_main}"
    return f"Search value {search} is not found in {arr_main}"

def update_element(arr_main):
    print(arr_main)
    print("Enter index at which you want to update the value")
    index = int(input())
    if index >= len(arr_main):
        return "Please Enter valid Index error `IndexError: list assignment index out of range`"
    print("Enter value which you want to update the value")
    val = int(input())
    arr_main[index] = val
    return arr_main

if __name__ == '__main__':
    arr_main = []
    choice = 1 

    while choice!=6:
        print("********** Menu Driven Program Array *****************")
        print("Menu")
        print("1: Display")
        print("2: Insertion")
        print("3: Deletion")
        print("4: Search")
        print("5: Update")
        print("6: Exit")

        print("Please Enter Choice")
        choice = int(input())

        if choice == 1:
            display_elements(arr_main)
        elif choice == 2:
            insert_element(arr_main)
        elif choice == 3:
            delete_element(arr_main)
            print(arr_main)
        elif choice == 4:
            print(search_element(arr_main))
        elif choice == 5:
            print(update_element(arr_main))
            