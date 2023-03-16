

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
#         self.width = float(input('Enter the length of the rectangle:'))
#         self.lenght = float(input('Enter the length of the rectangle:'))

#     def area(self):
#         return self.width * self.lenght


# class Square(Rectangle):
#     def __init__(self, name, sides):
#         super().__init__(name, sides)
#         self.lenght = float(input('Enter the length of the square:'))

#     def ares(self):
#         return self.lenght ** 2


# rectangle = Rectangle('Rectangle', 4)
# print("The area of the rectangle is:", rectangle.area())


# square = Square("Square", 4)
# print('Enter the area of the square:', square.area())


# // Task Nr.2
