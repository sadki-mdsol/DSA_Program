def likes(names):
    people = ""
    if len(names) == 0:
        people = "no one"

    for i in range(len(names)):
        # if len(names) == 1:
        #     people = names[i]
        people = people + names[i]
        if i == len(names)-2 and len(names)!=1:
            people = people + ' and '
        elif i< len(names)-2:
            people = people +', '
        
        # if len(names) == 1:
        #     people += names[i]
        # elif i == len(names)-1:
        #     people = people +" and " + names[i]
        # elif i< len(names)-1:
        #     people = people+ names[i]+", "
        

    return people+" likes it"

print(likes([]))
print(likes(['Peter']))
print(likes(['Peter','Jerry']))
print(likes(['Peter','Jerry','Jan']))
