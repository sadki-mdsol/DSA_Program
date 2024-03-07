class TreeNode:
    def __init__(self,data):
        self.parent= None
        self.children=[]
        self.data=data

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p :
            level = level+1
            p = p.parent
        return level

    def print_tree(self):
        # spaces = "|" 
        spaces = " "*(self.get_level()*3)
        prefix = spaces+"|__" if self.parent else ""
        print(prefix + self.data)

        if len(self.children) > 0:
            for chld in self.children:
                chld.print_tree()

def build_roduct_tree ():
    root = TreeNode('Electronics')

    lap = TreeNode('laptop')

    mac = TreeNode('Mac')
    MS = TreeNode('MS')
    TinkPad = TreeNode('ThinkPad')
    lap.add_child(mac)
    lap.add_child(MS)
    lap.add_child(TinkPad)
    root.add_child(lap)

    cp = TreeNode('Cell Phone')
    ip = TreeNode('iPhone')
    gp = TreeNode('Google Phone')
    vp = TreeNode('Vivo Phone')
    cp.add_child(ip)
    cp.add_child(gp)
    cp.add_child(vp)

    root.add_child(cp)

    tv = TreeNode('Television')
    sg = TreeNode('SAMSUNG')
    lg = TreeNode('LG')

    tv.add_child(sg)
    tv.add_child(lg)

    root.add_child(tv)

    return root

if __name__ =='__main__':
    root = build_roduct_tree()
    root.print_tree()