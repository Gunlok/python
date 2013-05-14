class Queue(object):
    def __init__(self):
        self.data=[]
        self.head=0
        self.tail=0
        self.count=0

    def enqueue(self, num):
        self.data.append(num)
        self.tail += 1
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return False

        ret = self.data[self.head]
        self.head+=1
        self.count-=1
        return ret

    def print_queue(self):
        for i in range(0, self.count):
            print self.data[self.head+i]
