from abc import ABC, abstractmethod


from Engine.engine import *
from Battery.battery import *

class Car(ABC):
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    @abstractmethod
    def needs_service(self):
        pass

