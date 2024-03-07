class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_chid(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p :
            p = p.parent
            level +=1
        return level

    def display_tree(self):
        space = " "*(self.get_level()*6)
        space = space + "|--"
        print(space + self.data)
        if len(self.children) > 0:
            for chld in self.children:
                chld.display_tree()

if __name__ =='__main__':
    choice = 0
    while choice <=5:
        print("Menu")
        print("1: Create Root Node Node")
        print("2: Create Child Node")
        print("3: Display Tree")
        choice = int(input("Enter Choice"))
        if choice ==1:
            root = TreeNode(input("Enter value for the Node"))
        elif choice ==2:
            node = TreeNode(input("Enter Childe Node Value"))
            root.add_chid(node)
        elif choice ==3:
            root.display_tree()

        print(root)