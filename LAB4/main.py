#EXERCITIU 1
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

'''
stack = Stack()
stack.push(32)
stack.push(4)
print(stack.stack)
stack.pop()
print(stack.stack)
print(stack.peek())
stack.pop()
print(stack.stack)
print(stack.peek())
'''


#EXERCITIU 2
class Queue:
    def __init__(self):
        self.queue = []

    def push(self,element):
        self.queue.append(element)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

'''
queue = Queue()
queue.push(12)
queue.push(13)
print(queue.queue)
print(queue.peek())
queue.pop()
print(queue.queue)
print(queue.peek())
queue.pop()
print(queue.queue)
print(queue.peek())
'''


#EXERCITIU 3
class Matrix:
    def __init__(self,n,m):
        self.rows = n
        self.cols = m
        self.matrix = [[0] * self.cols for _ in range(self.rows)]

    def getAll(self):
        return self.matrix

    def getElement(self, i, j):
        return self.matrix[i][j]

    def setElement(self, i, j, value):
        self.matrix[i][j] = value

    def traspose(self):
        transpose_matrix = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        self.matrix = transpose_matrix
        self.cols, self.rows = self.rows, self.cols

matrix1 = Matrix(2,3)
matrix1.setElement(0, 0, 1)
matrix1.setElement(0, 1, 2)
matrix1.setElement(0, 2, 3)
matrix1.setElement(1, 0, 4)
matrix1.setElement(1, 1, 5)
matrix1.setElement(1, 2, 6)

print(matrix1.getAll())

matrix1.traspose()
print(matrix1.getAll())

matrix1.traspose()
print(matrix1.getAll())