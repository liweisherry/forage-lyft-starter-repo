from abc import ABC, abstractmethod


from Engine.Engine import *
from Battery.Battery import *

class Car(ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self._engine = None
        self._battery = None

        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    # @abstractmethod
    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service()


class Calliope(Car):
    def __init__(self):
        self._engine = CapuletEngine(self.last_service_date, self.current_mileage,self.last_service_mileage)
        self._battery = Spindler(self.last_service_date)

class Glissade(Car):
    def __init__(self):
        self._engine = WilloughbyEngine(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self._battery = Spindler(self.last_service_date)


class Palindrome(Car):
    def __init__(self):
        self._engine = SternmanEngine(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self._battery = Spindler(self.last_service_date)


class Rorschach(Car):
    def __init__(self):
        self._engine = WilloughbyEngine(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self._battery = Nubbin(self.last_service_date)


class Thovex(Car):
    def __init__(self):
        self._engine = CapuletEngine(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self._battery = Nubbin(self.last_service_date)