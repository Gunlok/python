class Node(object):
    def __init__(self, key):
        self.key=key
        self.parent=None
        self.left=None
        self.right=None
        self.height = 0
    #----------------------------------------------------------
    def print_node(self):
        print self.key,
        if self.left!=None:
            self.left.print_node()
        if self.right!=None:
            self.right.print_node()
    #----------------------------------------------------------
    def is_balanced(self):
        return (self.left.height if self.left else -1) - (self.right.height if self.right else -1)
    
            

class AVL(object):
    def __init__(self):
        self.root = None

    def recomupte_height(self, from_node):
        changed = True
        node = from_node
        while node and changed:
            old_height = node.height
            node.height = (
        

    
