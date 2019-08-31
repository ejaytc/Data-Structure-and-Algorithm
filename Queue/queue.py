class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]

    def queueSize(self):
        return len(self.queue)

queue = Queue()
for i in range(5):
    queue.enqueue(i)
    print("enqueue: %d" % i)


queue.dequeue()
queue.dequeue()
queue.dequeue()

print("Peek: %d" % queue.peek())
print("Size: %d" % queue.queueSize())
