from abc import abstractmethod
from datetime import date

from Battery import Battery

from car import *


class CarFactory(object):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.current_date = date.today()

    def create_calliope(self):
        return Calliope()

    def create_glissade(self):
        return Glissade()

    def create_palindrome(self):
        return Palindrome()

    def create_rorschach(self):
        return Rorschach()

    def create_thovex(self):
        return Thovex()
