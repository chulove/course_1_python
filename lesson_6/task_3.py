class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus, department):
        super().__init__(name, surname, position, wage, bonus)
        self.department = department

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


emp_1 = Position("Иван", "Иванов", "Старший специалист", 100000, 10000, "Отдел кадров")
emp_2 = Position("Петр", "Петров", "Начальник отдела", 130000, 50000, "Отдел кадров")
print(emp_1.get_full_name())
print(emp_2.get_full_name())
print(emp_1.get_total_income())
print(emp_2.get_total_income())
