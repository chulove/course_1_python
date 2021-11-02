import re


class Complex:
    def __init__(self, complex):
        if type(complex) == str and re.search(r'^\-?\d+(\+|\-)\d+i$', complex.replace(' ', '')):
            self.r, self.i = map(int, re.findall(r'\-?\d+', complex.replace(' ', '')))
        elif type(complex) == str and re.search(r'^\-?\d+$', complex.replace(' ', '')):
            self.r, self.i = int(complex.replace(' ', '')), 0
        elif type(complex) == str and re.search(r'^\-?\d+i$', complex.replace(' ', '')):
            self.r, self.i = 0, int(complex.replace(' ', '')[:-1])
        else:
            raise ValueError('Invalid input')

    def __str__(self):
        return (str(self.r) * int(self.r != 0) + '+' * int(self.i > 0) + str(self.i) * int(self.i != 0) +
                'i').replace('+', ' + ').replace('-', ' - ').strip()

    def __add__(self, other):
        return Complex(str(self.r + other.r) + '+' * int(self.i + other.i >= 0) + str(self.i + other.i) + 'i')

    def __mul__(self, other):
        return Complex(
            str(self.r * other.r - self.i * other.i) + '+' * int(self.i * other.r + self.r * other.i >= 0)
            + str(self.i * other.r + self.r * other.i) + 'i')


a = Complex('-2+5i')
b = Complex('5i')
c = Complex('3')
d = Complex('1-6i')
print(a + b)
print(c * b)
print(a * d)
