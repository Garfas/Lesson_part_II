# 2023 03 28
# Lesson: Functional Programming Intro

# def say_hello() ->None:
#     print("hello")
    
# greet = say_hello

# greet() #print "hello"

# from collections.abc import Callable

# def say_hello(name: str) -> None:
#   print(f"hello {name}")

# def another_function(f: Callable, *args) -> None:
#   f(*args)

# another_function(say_hello, "mantas")


# def outer():
#     print("I am function outer()!")
    
#     def inner():
#         print("I am function inner()!")

#     # Function outer() returns function inner()
#     return inner

# function = outer()
# print(function)
# # <function outer.<locals>.inner at 0x7f18bc85faf0>
# function()
# # I am function inner()!

# outer()()
# # I am function inner()!

# animals = ["ferret", "vole", "dog", "gecko"]
# print(sorted(animals))
# # ['dog', 'ferret', 'gecko', 'vole']

# animals = ["ferret", "vole", "dog", "gecko"]
# def reverse_len(string: str) -> int:
#     return -len(string)

# print(sorted(animals, key=reverse_len))
# ['dog', 'ferret', 'gecko', 'vole']

# animals = ["ferret", "vole", "dog", "gecko"]
# print(sorted(animals, key=lambda s: -len(s)))
# # ['ferret', 'gecko', 'vole', 'dog']



# def reverse(s):
#     return s[::-1]

# print(reverse("I am a string"))
# # 'gnirts a ma I'

# reverse = lambda s: s[::-1]
# print(reverse("I am a string"))
# # 'gnirts a ma I'




# print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6))
# # 7.0
# print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(1.4, 1.1, 0.5))
# # 1.0



# from typing import Tuple

# def func(x) -> Tuple[int]:
#     return x, x ** 2, x ** 3

# print(func(2))
# # (2, 4, 16)

# print((lambda s: {s, s**2, s**3})(2))



# print(f"--- {(lambda s: s[::-1])('hello')} ---")


# map(<f>, <iterable>)

# def reverse(s):
#     return s[::-1]

# print(reverse("I am a string"))

# animals = ["cat", "dog", "hedgehog", "gecko"]
# iterator = map(reverse, animals)
# print(iterator)
# # <map object at 0x7fd3558cbef0>


# def f(a, b, c):
#     return a + b + c

# print(list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300])))
# # [111, 222, 333]

# Task Nr.1 Lambdas section:
#Write a Python program to find if a given string starts with a given character using Lambda. Sample Output: True False

start_with = lambda string, char: True if string.startswith(char) else False
#jei prasideda pirma raide True Jei ne false

print(start_with("hello world", "h"))#True
print(start_with("apple", "p"))#false

# Task Nr.2 Lambdas section:
#Write a Python program to create a lambda function that adds 15 to a given number passed  in as an \
    # argument, also create a lambda function that multiplies argument x with argument y and print the result.
    
add_fifteen = lambda x: x + 15 # arguments x=5
multiply = lambda x, y: x*y # arguments x=3, y=4

print(add_fifteen(5)) #20
print(multiply(3, 4)) #12 

# Task Nr.3 Lambdas section:
#Write a Python program to add two given lists using map and lambda.

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

add_lists = lambda x, y: x + y
result = list(map(add_lists, list_1, list_2)) # 5, 7, 9

print(result)

# Task Nr.4 Lambdas section:
#Write a Python program to square and cube every number in a given list of integers using Lambda

number = [1, 2, 3, 4, 5]

square_numbers = list(map(lambda x: x**2, number))
cube_number = list(map(lambda x: x**3, number))
    
print(square_numbers) #[1, 4, 9, 16, 25]
print(cube_number) # [1, 8, 27, 64, 125]


# Task Nr.5 Lambdas section:
# Write a Python program to extract year, month, date and time using Lambda. \
    # Sample Output: 2020-01-15 09:03:32.744178 2020 1 15 09:03:32.744178
    
from datetime import datetime

current_time = datetime.now()

get_year = lambda x: x.year
get_month = lambda x: x.month
get_date = lambda x: x.day # su date neveikia turi būti day
get_time = lambda x: x.strftime("%H:%M:%S:%f")

year = get_year(current_time)
month = get_month(current_time)
date = get_date(current_time)
time = get_time(current_time)

print(current_time)
print(year, month, date, time)


# Task Nr.1 Sorted section:
# Write a Python program to sort a list of tuples using Lambda. Original list of tuples: [('English', 88), ('Science', 90), \
    # ('Maths', 97), ('Social sciences', 82)] Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), \
        # ('Science', 90), ('Maths', 97)]



