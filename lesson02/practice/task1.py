class Car:

    def __init__(self, cars_brand, color, doors, volume_tank, number_of_wheels):

        self.cars_brand = cars_brand
        self.color = color
        self.doors = doors
        self.volume_tank = volume_tank
        self.number_of_wheels = number_of_wheels

    def drive(self):
        return f'I drive the car {self.cars_brand} {self.color} цвета'

    def __str__(self):
        return f'Марка: {self.cars_brand}\nЦвет: {self.color}\nОбъем бака: {self.volume_tank} литров'



class PassengerCar(Car):

    def __init__(self, cars_brand, color, doors, volume_tank, number_of_wheels, number_of_passengers):
        super().__init__(cars_brand, color, doors, volume_tank, number_of_wheels)
        self.number_of_passengers = number_of_passengers

    def drive(self):
        return f'Я еду на {self.cars_brand} {self.color} цвета и везу {self.number_of_passengers} пасажиров'


class Truck(Car):

    def __init__(self, cars_brand, color, doors, volume_tank, number_of_wheels, carrying_capacity, cargo):
        super().__init__(cars_brand, color, doors, volume_tank, number_of_wheels)
        self.carrying_capacity = carrying_capacity
        self.cargo = cargo

    def drive(self):
        return f'Я еду на {self.cars_brand} {self.color} цвета и везу {self.carrying_capacity} тонн {self.cargo}'

car1 = PassengerCar('BMW', 'Black', 4, 55, 4, 3)
car2 = Truck('DAF', 'White', 2, 150, 6, 10, 'Песок')
car3 = Truck('Камаз', 'Blue', 2, 150, 6, 7, 'Щебень')
print(car1)
print(car1.drive())
print()
print(car2)
print(car2.drive())
print()
print(car3)
print(car3.drive())