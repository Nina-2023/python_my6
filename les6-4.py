class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} движется со скоростью {self.speed} км/ч - превышение скорости!')
        else:
            print(f'{self.name} движется со скоростью {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} движется со скоростью {self.speed} км/ч - превышение скорости!')
        else:
            print(f'{self.name} движется со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    pass
car1 = TownCar(80, 'белый', 'Ford', False)
car2 = WorkCar(30, 'черный', 'Toyota', False)

print(car1.speed, car1.color, car1.name, car1.is_police)
print(car2.speed, car2.color, car2.name, car2.is_police)

car1.go()
car2.stop()
car1.turn('налево')
car2.show_speed()