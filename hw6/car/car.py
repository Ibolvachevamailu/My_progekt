import hw6.base
from hw6 import exceptions
import hw6.engine.Engine
from hw6.exceptions import start
from hw6.exceptions import MyException


class Car(hw6.base.Vehicle):

    def __init__(self, distance: int, weight = 1000, fuel = 1, fuel_consumption = 5, started_status = False):
        super().__init__(distance, weight, fuel, fuel_consumption, started_status)



    def start(self):
        if self.started_status and self.fuel > 0:
            self.started_status = 'started'
            return self.fuel
        else:
            raise MyException

    def move(self):
        n = self.fuel_consumption * self.distance
        if n < self.fuel:
            print(f'топлива достаточно - {self.fuel}л, расх на км {self.fuel_consumption}, всего км {self.distance} ')
        else:
            self.fuel = n
            print(f'данные по топливу обновлены: {self.fuel}л')
            raise exceptions.NotEnoughFuel
        print(f'топлива в итоге {self.fuel}л')

    def __str__(self):
        return f'вес: - {self.weight} кг\nтопливо: {self.fuel} литров\nрасход топлива: {self.fuel_consumption}л на км\nдистанция: {self.distance}\nстатус старта: {self.started_status}'


car1 = Car(623)

car1.start()
# car1.move()
# print(car)
# print(hw6.engine.Engine.engine1.set_engine)
# hw6.engine.Engine.engine1._volume = 100
# print(hw6.engine.Engine.engine1)
# print(hw6.engine.Engine.engine1.set_engine)







