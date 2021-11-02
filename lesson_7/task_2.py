from abc import ABC, abstractmethod


class Clothes(ABC):
    total_its = 0
    total_exp = 0

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Clothes.total_its += 1
        Clothes.total_exp += self.expense

    def __str__(self):
        return f'Сшито пальто. Размер - {self.size}, расход материала - {self.expense} кв.м.\n' \
               f'Всего сшито {Clothes.total_its} предмет(ов) одежды, общий расход материала - {Clothes.total_exp} кв.м.'

    @property
    def expense(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Clothes.total_its += 1
        Clothes.total_exp += self.expense

    def __str__(self):
        return f'Сшит костюм. Рост - {self.height}, расход материала - {self.expense} кв.м.\n' \
               f'Всего сшито {Clothes.total_its} предмет(ов) одежды, общий расход материала - {Clothes.total_exp} кв.м.'

    @property
    def expense(self):
        return round(self.height * 2 + 0.3, 2)


c1 = Coat(26)
c2 = Coat(31)
c3 = Suit(1.78)
c4 = Suit(1.83)

print(c4)
