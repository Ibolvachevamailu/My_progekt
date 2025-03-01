import traceback



class MyException(Exception):
    pass

class LowFuelError(MyException):
    pass

class NotEnoughFuel(MyException):
    pass

class CargoOverload(MyException):
    pass

# try:
#     fuel = hw6.base.Vehicle.fuel
#     if fuel <= 0:
#        raise LowFuelError
#     else:
#         raise NotEnoughFuel

try:
    f = start()
    if f <= 0:
        raise LowFuelError
    else:
        raise MyException

except LowFuelError:
    print(f'мало топлива')
except NotEnoughFuel:
    print(f'недостаточно топлива')
except CargoOverload:
    print(f'Перегрузка груза')
except Exception as e:#доб трейсбек
    print(f'ошибка: {traceback.format_exc()}')

#
# try:
#     weight = int(input('введите вес груза: '))
#     if weight >= 300:
#         raise CargoOverload
#     else:
#         print("Груз принят")
# except CargoOverload:
#     print(f'Перегрузка груза')
# except Exception as e:
#     print(f'ошибка: {traceback.format_exc()}')

