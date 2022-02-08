from Battery.Nubbin import Nubbin
from Battery.Spindler import Spindler
from Engine.capulet_engine import CapuletEngine
from Engine.sternman_engine import SternmanEngine
from Engine.willoughby_engine import WilloughbyEngine
from Tire.CarriganTire import CarriganTire

from Tire.OctoprimeTire import OctoprimeTire
from car import *


class CarFactory(object):
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, sensor_values):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date,last_service_date)
        tire = CarriganTire(sensor_values)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, sensor_values):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tire = OctoprimeTire(sensor_values)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, sensor_values):
        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler(current_date, last_service_date)
        tire = CarriganTire(sensor_values)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, sensor_values):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tire = OctoprimeTire(sensor_values)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, sensor_values):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tire = CarriganTire(sensor_values)
        car = Car(engine, battery, tire)
        return car