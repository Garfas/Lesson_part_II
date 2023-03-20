# 2023_03_14

# Task Nr.1: Fix these coding examples according to the standards we learnt during this lecture:
# class Person():
#     def __init__(self, name: str, surname: str) -> None:
#         self.name = name
#         self.surname = surname

#     def say_hello(self):
#         print(f"hello, {self.name} {self.surname}")


# person = Person("first", "person")
# person.say_hello()


# def greet_person(full_name: str) -> None:
#     """Function greets a person given full name as a string"""

#     print(
#         f"Hello {full_name.split()[0]} {full_name.split()[1]}, How are you today?")

# greet_person("Mantas Jankauskas")


# def greet_user(age: int) -> str:
#     eligible_to_enter = age >= 21

#     if eligible_to_enter == True:
#         return ("Welcome")
#     if eligible_to_enter == False:
#         return ("Access denied")


# print(greet_user)


# Write a python function that takes in one parameter - integer and then
# returns True if number is magic number
# or False if it is not a magic number


# def is_magic_number(num: int) -> bool:
#     while num > 9:
#         sum_of_digits = 0
#         for digit in str(num):
#             sum_of_digits += int(digit)
#         num = sum_of_digits
#     return num == 1


# print(is_magic_number(46))
# print(is_magic_number(17))
# print(is_magic_number(91))
# print(is_magic_number(179))
# print(is_magic_number(7))
# print(is_magic_number(123456789))
# print(is_magic_number(1234))
