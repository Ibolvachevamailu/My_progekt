from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self,distance: int, weight=1000, fuel=0, fuel_consumption=5, started_status=False):
        self.distance = distance
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started_status = started_status



    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def __str__(self):
        return f'состоянее: {self.started}\nтоплива {self.fuel} литров,\nвес {self.weight} кг'
