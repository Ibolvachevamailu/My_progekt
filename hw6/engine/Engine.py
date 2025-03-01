from dataclasses import dataclass


@dataclass

class Engine:
    _volume: int
    _pistons: int

    def __hash__(self):
        return hash(f'двигатель: {self._pistons}')
    #
    # def engin(self):
    #     return self._volume * self._pistons

    @property
    def set_engine(self):
        return self._volume * self._pistons

    @set_engine.setter
    def set_engine(self, value3):
        if value <= 0 or value2 <= 0:
            raise ValueError("Объем двигателя должен быть положительным")
        self._volume = value
        self._pistons = value2
        value3 = self._volume * self._pistons




# Проверяем
engine1 = Engine(6, 5)
# result_eng = engine1.engin()
# print(result_eng)
engine2 = Engine(3, 6)
# print(engine1 == engine2)


