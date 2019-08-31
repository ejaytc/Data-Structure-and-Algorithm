class Node:

    def __init__(self, data):
        self.data       = data
        self.nextNode   = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        newNode = Node(data)
        self.size += 1

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self, data):

        if self.head is None:
            return
        
        self.size -= 1
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    def linklistSize(self):
        return self.size
    
    def linklistSize_(self):
        actualNode = self.head
        size = 0
        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
            print(actualNode)

        return size

    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
    
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode
    
    def traverseList(self):

        actualNode = self.head
        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode


linklist = LinkedList()
for i in range(10):
    if i < 5:
        linklist.insertStart(i)
    else:
        linklist.insertEnd(i)


linklist.traverseList()
print("size: %d" % linklist.linklistSize())

for i in range(10):
    linklist.remove(i)

print("After remove:\n")
linklist.traverseList()
print("size: %d" % linklist.linklistSize())