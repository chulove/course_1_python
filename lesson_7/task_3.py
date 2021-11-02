class Cell:
    def __init__(self, units):
        if type(units) == int:
            self.units = units
        else:
            raise ValueError('Cell units number can only be a natural integer')

    def __str__(self):
        return f'Cell contents {self.units} units'

    def __add__(self, other):
        return Cell(self.units + other.units)

    def __sub__(self, other):
        if self.units > other.units:
            return Cell(self.units - other.units)
        else:
            raise ValueError('subtraction is defined for two cells only if the first one is greater than second')

    def __mul__(self, other):
        return Cell(self.units * other.units)

    def __truediv__(self, other):
        return Cell(self.units // other.units)

    def make_order(self, length=1):
        if type(length) == int:
            return f"{'*' * length}\n" * (self.units // length) + '*' * (self.units % length)
        else:
            raise ValueError('length can only be a natural integer')


c1 = Cell(11)
c2 = Cell(9)
print(c1 / c2)
print(c1.make_order(3))
