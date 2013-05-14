class Node(object):
    def __init__(self, key):
        self.key=key
        self.parent=None
        self.left=None
        self.right=None
    #----------------------------------------------------------
    def print_node(self):
        print self.key,
        if self.left!=None:
            self.left.print_node()
        if self.right!=None:
            self.right.print_node()
    

class BinarySearchTree(object):    
    def __init__(self):
        self.data=[]
        self.top=None
    #----------------------------------------------------------
    def insert(self, node):
        if self.top==None:
            self.top=node
            return

        position = self.top
        while position!=None:
            if position.key > node.key:
                if position.left == None:
                    position.left = node
                    node.parent = position
                    return
                position=position.left
            else:
                if position.right == None:
                    position.right = node
                    node.parent = position
                    return
                position=position.right
    #-------------------------------------------------------------
    def search(self, key):
        if self.top==None:
            return False

        position = self.top
        while position!=None:
            if position.key == key:
                return True
            if position.key > key:
                position=position.left
                continue
            else:
                position=position.right
                continue
        return False
    #---------------------------------------------------------------
    def remove(self, key):
        if not self.search(key):
            return

        position=self.top
        while True:
            if position.key==key:
                # Option 1 - no child
                if position.left==None and position.right==None:
                    if position.parent.key > key:
                        position.parent.left=None
                        break
                    else:
                        position.parent.right=None
                        break
                # Option 2 - One child
                if position.left!=None and position.right==None:
                    position.key = position.left.key
                    position.left=None
                    break
                if position.left==None and position.right!=None:
                    position.key = position.right.key
                    position.right=None
                    break
                #Option 3 - has both children - swap with leftest of right tree and remove it
                leftest = position.right
                while leftest.left!=None:
                    leftest=leftest.left
                position.key=leftest.key
                leftest.parent.left=None                
                break
            # Else search it
            if position.key>key:
                position=position.left
                continue
            else:
                position=position.right
    #-----------------------------------------------------------------------
    def print_tree(self):
        self.top.print_node()
        
