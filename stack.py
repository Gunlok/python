class Stack(object):
    def __init__(self):
        self.data=[]

    def push(self, num):
        self.data.append(num)

    def back(self):
        if self.data==[]:
            return False

        return self.data[len(self.data)-1]

    def pop(self):
        if self.data==[]:
            return False

        ret = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        return ret

    def print_stack(self):
        self.backup=self.data
        length = len(self.data)
        for i in range(0, length):
            print self.data.pop(),

        print

        self.data=self.backup
