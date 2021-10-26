class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


stationery = Stationery("Канцелярская принадлежность")
pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
