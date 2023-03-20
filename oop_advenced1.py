# 2023_03_15

# class A:
#     def foo(self) -> None:
#         print("A.foo")


# class B(A):
#     def foo(self) -> None:
#         print("B.foo")


# class C(A):
#     def foo(self) -> None:
#         print("C.foo")


# class D(C, B):
#     pass


# d = D()
# d.foo()  # prints "B.foo"

# print(D.__mro__)
# # foo arba foobar, foorbar


# //Task Nr.1


# class Shape:
#     def __init__(self, name, sides):
#         self.name = name
#         self.sides = sides

#     def area(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, name, sides):
#         super().__init__(name, sides)
#         self.width = float(input("Enter the length of the rectangle:"))
#         self.lenght = float(input("Enter the length of the rectangle:"))

#     def area(self):
#         return self.width * self.lenght


# class Square(Rectangle):
#     def __init__(self, name, sides):
#         super().__init__(name, sides)
#         self.lenght = float(input("Enter the length of the square:"))

#     def ares(self):
#         return self.lenght**2


# rectangle = Rectangle("Rectangle", 4)
# print("The area of the rectangle is:", rectangle.area())


# square = Square("Square", 4)
# print("Enter the area of the square:", square.area())


# // Task Nr.2


class Vehile:
    def __init__(self, name, seatings_capacity, max_speed):
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
    def __init__(self, name, seatings_capacity, max_speed):
        super().__init__(name, seatings_capacity, max_speed)


class Taxi(Vehile):
    def __init__(self, name, seatings_capacity, max_speed):
        super().__init__(name, seatings_capacity, max_speed)

    def hail(self):
        print(f"{self.name} has been hailed.")

    def pay_fare(self):
        print(f"{self.name} has been paid the fare.")


class Train(Vehile):
    def __init__(
        self, name, seatings_capacity, max_speed, num_cars
    ):
        super().__init__(name, seatings_capacity, max_speed)
        self.num_cars = num_cars

    def announce_stop(self):
        print(f"{self.name} is  announcing its stops.")


bus = Bus("Bus", 50, 60)
print("Bus fare:", bus.fare_charge())

taxi = Taxi("Taxi", 4, 40)
taxi.hail()
taxi.accelerate()
taxi.pay_fare()

train = Train("Train", 500, 120, 10)
train.star()
train.accelerate()
train.stop()



# //Task Nr.5
# A self-driven electric car needs to make a delivery from point A to point B. The path consists of intervals with a traffic light at the end of each interval. Before the journey, the car calculates the expected, lucky, unlucky time travel estimates and uploads this information to the server.
# Travel through an interval can be modeled as having these parts:
#     Initial acceleration. The speed at t = 0 can be zero or any value less than cruising speed coming from the previous interval. The car accelerates to the cruising speed. If it is already at cruising speed, then it does not need to accelerate.
#     Cruising distance. The car travels at constant speed until the decision point. Stoppage distance is the length required for the car to drop its speed from cruising speed to zero. Decision point is at the end of interval minus the stoppage distance.
#     Deceleration. If the light is yellow or red, the car starts dropping the speed.
#     Second acceleration. If the light suddenly turns green before the car is completely stopped, it accelerates and exits the interval with some speed.
# If the light is green at the decision point, the car does not decelerate. It procced and exits the interval with cruising speed. If the light is yellow or red, the car stops at the end of the interval and continues to wait until the lights turns green. It enters the next interval with speed equal zero.
# The traffic lights are modeled as a random number from the inclusive interval e.g. (-59, 70). If the number is <= 0, the light is green. A positive number represents a number of seconds when the lights turn green after the car passes the decision point. For example if time_to_green == 2, the car will decelerate for 2 seconds, then switch to accelerating; if time_to_green == 50, the car will decelerate, stop and wait until 50 seconds pass since the decision point, then enters next interval with zero speed.
# Travel through the path is summation of travels through connected intervals. It can enter the next interval with non-zero speed if got lucky with the light. At the last interval time_to_green == stoppage_time, not random! In this way it’s guaranteed that the car arrived at the end of the path and stopped.
# Write the implementation of the class Route. It receives a dictionary with parameters of the car, intervals, lights cycle, and number of simulations. Description of three required methods is in the Code window. Per each simulation randomly generate n-1 time_to_green numbers to model the traffic lights, last interval has defined time_to_green.
# After having a sample of travel times compute: average, 5-percentile (lucky), 95-percentile (unlucky) of the sample.
