# 2023_03_16


class Vehile:
    def __init__(self, name: str, seatings_capacity: str, max_speed: str):
        self.name = name
        self.seatings_capacity = seatings_capacity
        self.max_speed = max_speed

    def star(self):
        print(f"{self.name} has started,")

    def stop(self):
        print(f"{self.name} has stoped,")

    def accelerate(self):
        print(f"{self.name} is accelarating,")

    def brake(self):
        print(f"{self.name} is braking.")

    def fare_charge(self):
        fare = self.seatings_capacity * 100
        if isinstance(self, Bus):
            fare *= 1.1
        return fare


class Bus(Vehile):
    def __init__(self, name: str, seatings_capacity: str, max_speed: str):
        super().__init__(name, seatings_capacity, max_speed)


class Taxi(Vehile):
    def __init__(self, name: str, seatings_capacity: str, max_speed: str):
        super().__init__(name, seatings_capacity, max_speed)

    def hail(self):
        print(f"{self.name} has been hailed.")

    def pay_fare(self):
        print(f"{self.name} has been paid the fare.")


class Train(Vehile):
    def __init__(
        self, name: str, seatings_capacity: str, max_speed: str, num_cars: str
    ):
        super().__init__(name, seatings_capacity, max_speed)
        self.num_cars = num_cars

    def announce_stop(self):
        print(f"{self.name}")
