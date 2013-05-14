class MinHeap(object):
    def __init__(self):
        self.data=[]

    def siftUp(self, index):
        if index == 0:
            return
        parent_index = (index-1)/2

        if self.data[parent_index]>self.data[index]:
            self.data[parent_index],self.data[index]=self.data[index],self.data[parent_index]
            self.siftUp(parent_index)    

    def insert(self, num):
        self.data.append(num)
        self.siftUp(len(self.data)-1)

    def siftDown(self, index):
           minVal = self.data[index]
           minValIndex = index

           if 2*index+1 < len(self.data) and self.data[2*index+1] < minVal:
               minVal = self.data[2*index+1]
               minValIndex = 2*index+1

           if 2*index+2 < len(self.data) and self.data[2*index+2] < minVal:
               minVal = self.data[2*index+2]
               minValIndex = 2*index+2

           if minValIndex == index:
               return

           #swap 
           self.data[minValIndex], self.data[index] = self.data[index], minVal
           self.siftDown(minValIndex)

    def extractMin(self):
           minimum = self.data[0]

           self.data[0] = self.data[-1]
           self.data.pop()

           if self.data!=[]:
               self.siftDown(0)

           return minimum

class MaxHeap(object):
    def __init__(self):
        self.data=[]

    def siftUp(self, index):
        if index == 0:
            return
        parent_index = (index-1)/2

        if self.data[parent_index]<self.data[index]:
            self.data[parent_index],self.data[index]=self.data[index],self.data[parent_index]
            self.siftUp(parent_index)    

    def insert(self, num):
        self.data.append(num)
        self.siftUp(len(self.data)-1)

    def siftDown(self, index):
           minVal = self.data[index]
           minValIndex = index

           if 2*index+1 < len(self.data) and self.data[2*index+1] > minVal:
               minVal = self.data[2*index+1]
               minValIndex = 2*index+1

           if 2*index+2 < len(self.data) and self.data[2*index+2] > minVal:
               minVal = self.data[2*index+2]
               minValIndex = 2*index+2

           if minValIndex == index:
               return

           #swap 
           self.data[minValIndex], self.data[index] = self.data[index], minVal
           self.siftDown(minValIndex)

    def extractMin(self):
           minimum = self.data[0]

           self.data[0] = self.data[-1]
           self.data.pop()

           if self.data!=[]:
               self.siftDown(0)

           return minimum
