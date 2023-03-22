# #2023_03_20

# from abc import ABC, abstractclassmethod

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     @abstractclassmethod
#     def speak(self):
#         return self.name

# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name
#         super().__init__(name=name)

#     def speak(self):
#         return "Dog say Woof"
    

# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
#         super().__init__(name=name)

#     def speak(self):
#         return "Cat say Meow"
    

# my_animal = Cat("murka")
# print(my_animal.speak())
# # print(my_animal.name())


#Task Nr.3
from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def get_area(self):
        pass

    @abstractclassmethod
    def get_perimeter(self):
        pass

    @abstractclassmethod
    def draw(self):
        pass

    def get_color(self,color):
        return "BLACK"
    
    def set_color(self,color):
        self.set_color = color
'''Subclass 1'''

class Circle(Shape):
    def __init__(self, radius):
            self.radius = radius

    def get_area(self):
            return 3.14*self.radius**2
        
    def get_perimeter(self):
            return 2*3.14*self.radius
        
    def draw(self):
            print(f'drawning a circle with radius {self.radius}')

# '''Subclass 2:'''

class Square(Shape):
    def __init__(self, side):
            self.side = side

    def get_area(self):
            return self.side**2
        
    def get_perimeter(self):
            return 4*self.side
        
    def draw(self):
        print(f'drawning a square with side {self.side}')


#Task Nr.4