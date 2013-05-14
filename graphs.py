class TableGraph(object):
    def __init__(self, setsize):
        self.size=setsize
        self.table=[[0]*self.size for x in range(self.size)]
        
    def addRoute(self, fro, to):
        self.table[fro][to]=1

    def deleteRoute(self, fro, to):
        self.table[fro][to]=0

    def access(self, fro, to):
        return self.table[fro][to]

    def printTable(self):
        print " |",
        for i in range(self.size):
            print str(i) + "|",
        print " "
        for i in range(self.size):
            print str(i) + "|",
            for j in range(self.size):
                print str(self.table[i][j]) + "|",
            print " "
#---------------------------------------------------#
class TableGraphWithCost(object):
    def __init__(self, setsize):
        self.size=setsize
        self.table=[[0]*self.size for x in range(self.size)]
        
    def addRoute(self, fro, to, cost):
        self.table[fro][to]=cost

    def deleteRoute(self, fro, to):
        self.table[fro][to]=0

    def access(self, fro, to):
        return self.table[fro][to]

    def printTable(self):
        print " |",
        for i in range(self.size):
            print str(i) + "|",
        print " "
        for i in range(self.size):
            print str(i) + "|",
            for j in range(self.size):
                print str(self.table[i][j]) + "|",
            print " "            

#---------- Neighbors Graph -------------------------#
class Node(object):
    def __init__(self, key):
        self.key=key
        self.neighbors=[]
        
    def addNeighbor(self, node):
        self.neighbors.append(node)

    def fromTable(self, table):
        for i in range(table.size):
            for j in range(table.size):
                if table.access(i, j) != 0:
                    self.neighbors.append(Node(table.access(i, j)))
    # do hloubky
    def DFSevaluate(self, done):
        if self not in done:
            print str(self.key) + " ",
            done.append(self)
            for i in self.neighbors:
                i.DFSevaluate(done)
            
    def printDFS(self):
        done = []
        print str(self.key) + " ",
        for i in self.neighbors:
            i.DFSevaluate(done)
            
    # do sirky
    def BFSevaluate(self, queue):
        queue += self.neighbors
    
    def printBFS(self):
        print self.key,
        queue = self.neighbors
        done = []
        for i in queue:
            if i not in done:
                print i.key,
                done.append(i)
                i.BFSevaluate(queue)
                
#---------- Neighbors Graph With Cost -----------------#
class NodeWithCost(object):
    def __init__(self, key):
        self.key=key
        self.neighbors=[]
        
    def addNeighbor(self, node, cost):
        self.neighbors.append([node, cost])

    def fromTable(self, table):
        for i in range(table.size):
            for j in range(table.size):
                if table.access(i, j) != 0:
                    self.neighbors.append(Node(table.access(i, j)))

    # do hloubky
    def DFSevaluate(self, done):
        if self not in done:
            print str(self.key) + " ",
            done.append(self)
            for i in self.neighbors:
                i[0].DFSevaluate(done)
            
    def printDFS(self):
        done = [self]
        print str(self.key) + " ",
        for i in self.neighbors:
            i[0].DFSevaluate(done)
            
    # do sirky
    def BFSevaluate(self, queue):
        queue += self.neighbors
    
    def printBFS(self):
        print self.key,
        queue = self.neighbors
        done = [self]
        for i in queue:
            if i[0] not in done:
                print i[0].key,
                done.append(i[0])
                i[0].BFSevaluate(queue)
