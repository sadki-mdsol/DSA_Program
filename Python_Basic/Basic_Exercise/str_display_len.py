def display_str(lst):
    for ele in lst:
        if len(ele) >5:
            print(ele)



lst_names =[]
for ele in range(10):
    lst_names.append(input("Enter Name"))

print(lst_names)
display_str(lst_names)