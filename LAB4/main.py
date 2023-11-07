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


#EXERCITIU 3
class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = [[0] * self.cols for _ in range(self.rows)]

    def get_all(self):
        return self.matrix

    def get_element(self, i, j):
        return self.matrix[i][j]

    def set_element(self, i, j, value):
        self.matrix[i][j] = value

    def multiply(self, another):
        if self.cols != another.rows:
            return None

        result = Matrix(self.rows, another.cols)

        for i in range(self.rows):
            for j in range(another.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * another.matrix[k][j]

        return result

    def transpose(self):
        transpose_matrix = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        self.matrix = transpose_matrix
        self.cols, self.rows = self.rows, self.cols

    def transform(self, transform):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = transform(self.matrix[i][j])

    def iterate(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                func(i, j, self.matrix[i][j])

    def iterate_lambda(self, func):
        self.iterate(lambda i, j, val: self.set_element(i, j, func(val)))