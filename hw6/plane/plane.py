import hw6.base
from hw6 import exceptions


class Plane(hw6.base.Vehicle):

    def __init__(self, cargo: int, max_cargo: int, distance: int, weight=1000, fuel=0, fuel_consumption=5, started_status=True):
        super().__init__(distance, weight, fuel, fuel_consumption, started_status)
        self.cargo = cargo
        self.max_cargo = max_cargo



    def start(self):
        if self.started_status and self.fuel > 0:
            self.started_status = 'started'
            return self.started_status
        else:
            raise exceptions.LowFuelError


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
        return f'вес: - {self.weight} кг\nтопливо: {self.fuel} литров\nрасстояние: {self.distance}\nрасход топлива: {self.fuel_consumption}л на 1 км\nстатус старта: {self.started_status}\nмаксимальный груз: {self.max_cargo}\nгруз: {self.cargo}'

    def load_cargo(self):
        if self.cargo < self.max_cargo:
            print('груз принят')
        else:
            n = self.max_cargo - self.cargo
            self.cargo = self.cargo + n
            print(f'перегруз на {n}кг')
            print(f'данные по грузу обновлены: {self.cargo}кг')
            raise exceptions.CargoOverload


    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo

plane = Plane(300, 233,100)
# print(plane)
# plane.start()
plane.move()
# plane.load_cargo()
# plane.remove_all_cargo()

# print(plane)










