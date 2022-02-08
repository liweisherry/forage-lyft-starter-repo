from abc import ABC

from Engine.engine import Engine
from car import Car


class SternmanEngine(Engine):
    def _init_(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
