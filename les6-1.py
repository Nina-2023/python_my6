import time
class TrafficLight:
    __color = None

    def running(self):
        self.__color = 'red'
        print("Цвет светофора: {}".format(self.__color))
        time

        self.__color = 'yellow'
        print("Цвет светофора: {}".format(self.__color))
        time.sleep(2)

        self.__color = 'green'
        print("Цвет светофора: {}".format(self.__color))
        time.sleep(3)


traffic_light = TrafficLight()
traffic_light.running()


