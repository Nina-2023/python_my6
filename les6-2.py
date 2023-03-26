class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, thickness):
        return self._length * self._width * thickness * 0.001


road = Road(1000, 10)
print(road.asphalt_mass(5))  # 5 метров толщины асфальта
# 50000.0