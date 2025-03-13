import hw6.base
from hw6.exceptions import LowFuelError, CargoOverload, NotEnoughFuel

class Plane(hw6.base.Vehicle):

    def __init__(self, cargo: int, max_cargo: int, distance: int, weight = 1000, fuel = 0, fuel_consumption = 5, started_status = 0):
        super().__init__(distance, weight, fuel, fuel_consumption, started_status)
        self.cargo = cargo
        self.max_cargo = max_cargo



    def start(self):
        if not self.started_status:
            if self.fuel > 0:
                self.started_status = True
        else:
            raise LowFuelError('мало топлива')


    def move(self):
        n = self.fuel_consumption * self.distance
        if n < self.fuel:
            print(f'топлива достаточно - {self.fuel}л, расход на км {self.fuel_consumption}, всего км {self.distance} ')
        else:
            self.fuel = n
            print(f'данные по топливу обновлены: {self.fuel}л')
            raise NotEnoughFuel('недостаточно топлива')
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
            raise CargoOverload('Перегрузка груза')


    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo

plane = Plane(300, 233,100)

plane.start()

# plane.move()
print(plane)
# plane.load_cargo()
# plane.remove_all_cargo()

# print(plane)










