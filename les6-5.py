class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f"Отрисовка ручкой цвета {self.color}")
class Pencil(Stationery):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f"Отрисовка карандашом цвета {self.color}")
class Marker(Stationery):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f"Отрисовка маркером цвета {self.color}")

pen = Pen("Ручка", "синий")
pen.draw()
pencil = Pencil("Карандаш", "черный")
pencil.draw()
marker = Marker("Маркер", "зеленый")
marker.draw()