from Battery.battery import Battery


class Nubbin(Battery):
    def _init_(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return True if self.last_service_date.replace(year=self.last_service_date.year + 4) < self.current_date else False
