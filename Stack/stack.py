class Stack:

    def __init__(self):
        self.stack = []

    def isEmpyt(self):
        return self.stack ==[]
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)



stack = Stack()
for i in range(5):
    stack.push(i)

stack.pop()
stack.pop()
print("Peek: %d" % stack.peek())
print("Size: %d" % stack.sizeStack())


