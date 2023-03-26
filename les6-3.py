class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

worker1 = Position('John', 'Smith', 'Manager', 10000, 2000)

print(worker1.name)
print(worker1.surname)
print(worker1.position)
print(worker1._income)

print(worker1.get_full_name())
print(worker1.get_total_income())