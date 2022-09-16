# class Car:
#     def __init__(self):
#         self.price=2000
#         self._speed = 0
#         self.__color = "red"
#     def get_color(self):
#         return self.__color
#     def set_color(self,color):
#         self.__color = color
#
# if __name__ == "__main__":
#     my_car = Car()
#     print(my_car.price)
#     print(my_car._speed)
#     # print(my_car.__color)
#     print(my_car.get_color())
#     my_car.set_color("blue")
#     print(my_car.get_color())
class Car:
    def __init__(self):
        self._price=0
        self._speed = 0
        self._color = None
    def get_price(self):
        return self._price
    def set_price(self,value):
        self._price = value
    def get_speed(self):
        return self._speed
    def set_speed(self,value):
        self._speed = value
    def get_color(self):
        return self._color
    def set_color(self,value):
        self._color = value

if __name__ == "__main__":
    my_car = Car()
    my_car.set_price(2000)
    my_car.set_speed(20)
    my_car.set_color("red")
    print("가격:",my_car.get_price())
    print("속도:",my_car.get_speed())
    print("색상:",my_car.get_color())