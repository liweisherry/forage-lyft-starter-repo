from Tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensor_values: list):
        self.sensor_values = sensor_values

    def needs_service(self):
        return True if sum(self.sensor_values) >= 3 else False
