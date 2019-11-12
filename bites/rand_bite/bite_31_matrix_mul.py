class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __matmul__(self, other):
        for line1, line2 in zip(self.matrix, other):
            line1[0] * line2[]

if __name__ == '__main__':
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[11, 12], [13, 14]])

