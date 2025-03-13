import hw6.base
import hw6.engine.Engine
from hw6.exceptions import LowFuelError



class Car(hw6.base.Vehicle):

    def __init__(self, distance: int, weight = 1000, fuel = 1, fuel_consumption = 10, started_status = False):
        super().__init__(distance, weight, fuel, fuel_consumption, started_status)

    def start(self):
        if self.fuel > 0:
            if self.started_status:
                self.started_status = True
            else:
                self.started_status = True
        else:
            raise LowFuelError(f"Недостаточно топлива для запуска двигателя")


    def move(self):
        n = self.fuel_consumption * self.distance
        if n < self.fuel:
            print(f'топлива достаточно - {self.fuel}л, расх на км {self.fuel_consumption}, всего км {self.distance} ')
        else:
            self.fuel = n
            print(f'данные по топливу обновлены: {self.fuel}л')
            raise NotEnoughFuel
        print(f'топлива в итоге {self.fuel}л')

    def __str__(self):
        return f'вес: - {self.weight} кг\nтопливо: {self.fuel} литров\nрасход топлива: {self.fuel_consumption}л на км\nдистанция: {self.distance}\nстатус старта: {self.started_status}'


car1 = Car(623)


car1.start()
print(car1)
# car1.move()
# print(car)
# print(hw6.engine.Engine.engine1.set_engine)
# hw6.engine.Engine.engine1._volume = 100
# print(hw6.engine.Engine.engine1)
# print(hw6.engine.Engine.engine1.set_engine)







