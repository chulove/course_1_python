from functools import reduce


class Matrix:
    def __init__(self, matrix):
        if matrix and reduce(lambda x, y: len(x) if len(x) == len(y) else 0, matrix):
            self.matrix = matrix
        else:
            raise ValueError('To define an n*m matrix, pass n lists/tuples with m elements')

    def __str__(self):
        return '\n'.join(['\t'.join([str(el) for el in row]) for row in self.matrix])

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            return Matrix([tuple(map(sum, zip(*row))) for row in zip(self.matrix, other.matrix)])
        else:
            raise ValueError('Matrix addition is defined for two matrices of the same dimensions')

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            return Matrix([tuple(map(lambda x, y: x - y, *row)) for row in zip(self.matrix, other.matrix)])
        else:
            raise ValueError('Matrix addition is defined for two matrices of the same dimensions')

    def transpose(self):
        self.matrix = tuple(zip(*self.matrix))

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Matrix([tuple(map(lambda x: x * other, row)) for row in self.matrix])
        elif type(other) == Matrix:
            if len(self.matrix[0]) == len(other.matrix):
                mtrx = []
                for i in range(len(self.matrix)):
                    row = []
                    for j in range(len(other.matrix[0])):
                        row.append(sum(map(lambda x, y: x * y, self.matrix[i], [k[j] for k in other.matrix])))
                    mtrx.append(row)
                return Matrix(mtrx)
            else:
                raise ValueError('Matrix multiplication is defined for two matrices of n*m and m*k dimensions')
        else:
            raise TypeError(f"unsupported operand type(s) for *: 'Matrix' and '{type(other)}'")

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return Matrix([tuple(map(lambda x: x * other, row)) for row in self.matrix])
        else:
            raise TypeError(f"unsupported operand type(s) for *: '{type(other)}' and 'Matrix'")


m1 = Matrix([(1, 2), (4, 5)])
m2 = Matrix([(10, 2), (14, 5)])
m3 = Matrix([(2, 3), (5, 6)])
m4 = Matrix([(2, 3, 4), (5, 6, 7)])

print(m1 + m2)
# print(m1+m3) # выдаст ошибку из-за размеров
print(m1 * 3 - m2)
print(m1 * m2)
print(m3 * m4)
# print(m4*m3) # выдаст ошибку из-за размеров
