from datetime import date


class Engine(object):
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return False


class CapuletEngine(Engine):
    def _init_(self):
        Engine.__init__(self)


    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000


class SternmanEngine(Engine):
    def _init_(self, warning_light_is_on):
        Engine.__init__(self)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False


class WilloughbyEngine(Engine):
    def _init_(self):
        Engine.__init__(self)

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
