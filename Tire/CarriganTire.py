from Tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensor_values: list):
        self.sensor_values = sensor_values

    def needs_service(self):
        for num in self.sensor_values:
            if num >= 0.9:
                return True
        return False
