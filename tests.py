from random import randint
import bst

def heapTest(heap):
    for i in range(10):
        rand = randint(0, 100)
        print rand,
        heap.insert(rand)
    print "\n"
    print heap.data
    print "\n"
    for i in range(10):
        print heap.extractMin(),

def stackTest(stack):
    for i in range(10):
        rand = randint(0, 100)
        print rand,
        stack.push(rand)
    print "\n"
    print stack.data
    print "\n"
    stack.print_stack()

def queueTest(queue):
    for i in range(10):
        rand = randint(0, 100)
        print rand,
        queue.enqueue(rand)
    print "\n"
    print queue.data
    print "\n"
    queue.print_queue()

def binarySearchTreeTest(tree):
    for i in range(23):
        rand = randint(0, 100)
        print rand,
        if tree.search(rand)==False:
            tree.insert(bst.Node(rand))
    tree.print_tree()
    delete = int(raw_input("Select key to delete: "))
    tree.remove(delete)
    tree.print_tree()
    








        
