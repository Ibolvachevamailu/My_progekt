# class CustomRange:
#
#     def __init__(self, value):
#         self.value = value
#         self.range = (self._get_range(self.value)) #здесь создаем м-д range
#
#     @staticmethod
#     def _get_range(n):
#         return print(list(range(n))) #сюда не опрокидывается сам объект (self) поэтому м-д статический
#
#
# num1 = CustomRange(10)
# print(num1.range) #обратились к м-ду range, созданному в инит
#
# my_dict = {}.fromkeys(list('123355'), None)
# print(my_dict)


class Human:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property #мы из м-да _age сделали атрибут, это геттер, то есть на него можно посмотреть но не использовать
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            salf._age = value
        else:
            print('возраст целое число')



    def __str__(self):
        return f'{self.name}: {self._age}' #м-д str выводит в читаемом виде д. пользователя
#
#
num2 = Human('Inna', 20)
# print(num2)
#
# # num2._age = 37
# # print(num2)
#
# num2.surname = 'no' #создали нов атрибут
# print(num2.__dict__)
#
num2.age = 'uyi'
print(num2.age)


class Human2(Human):
    pass

human2 = Human2('inna','l')
print(human2.age)

# print(human2.) = 37
print(human2.__dict__)