import hw6.base
from hw6.exceptions import LowFuelError, CargoOverload, NotEnoughFuel

class Plane(hw6.base.Vehicle):

    def __init__(self, cargo: int, max_cargo: int, distance: int, weight = 1000, fuel = 1, fuel_consumption = 5, started_status = False):
        super().__init__(distance, weight, fuel, fuel_consumption, started_status)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def start(self):
        if self.fuel > 0:
            if self.started_status:
                self.started_status = True#поменять на стартед
            else:
                self.started_status = True
        else:
            raise LowFuelError(f"Недостаточно топлива для запуска двигателя")

    def move(self):
        n = self.fuel_consumption * self.distance
        if self.fuel >= n:
            print(f'топлива достаточно - {self.fuel}л, расход на км {self.fuel_consumption}, всего км {self.distance} ')
        elif self.fuel < n:
            self.fuel = n
        else:
            raise NotEnoughFuel('недостаточно топлива')
        print(f'топлива в итоге {self.fuel}л')

    def __str__(self):
        return f'вес: {self.weight} кг\nтопливо: {self.fuel} литров\nрасстояние: {self.distance}\nрасход топлива: {self.fuel_consumption}л на 1 км\nстатус старта: {self.started_status}\nмаксимальный груз: {self.max_cargo}\nгруз: {self.cargo}'

    def load_cargo(self):
        if self.cargo <= self.max_cargo:
            print('груз принят')
        elif self.cargo > self.max_cargo:
            n = self.max_cargo - self.cargo
            print(f'перегруз на {n}кг')
            self.cargo = self.cargo + n
            print(f'данные по грузу обновлены: {self.cargo}кг')
        else:
            raise CargoOverload('Перегрузка груза')

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo

plane = Plane(300, 200,100)
# print(plane)
# plane.start()
# plane.move()

# plane.load_cargo()
# plane.remove_all_cargo()











