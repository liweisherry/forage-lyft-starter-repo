from datetime import date


class Battery(object):
    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date
        self.current_date = date.today()

    def needs_service(self):
        return False


class Spindler(Battery):
    def _init_(self):
        Battery.__init__(self)

    def needs_service(self):
        return self.current_date.year - self.last_service_date.year > 2


class Nubbin(Battery):
    def _init_(self):
        Battery.__init__(self)

    def needs_service(self):
        return self.current_date.year - self.last_service_date.year > 4
