# 2023.03.30
# OOP Advanced [lesson5]: Class instance, static methods.

# Task Nr.1
# Create a class which takes temperature measurements in Kelvins and add static methods to\
    # transform those to Celsius and Fahrenheit units. Use OOP abstraction.


# from abc import ABC, abstractclassmethod

# class TemperatureConverter (ABC):
#     @staticmethod
 
#     def kelvin_to_Celsius(kelvin):
#         pass
    
#     @staticmethod
  
#     def kelvin_to_fahrenheit(kelvin):
#         pass
    
# Class Temperature(TemperatureConverter):
    
#     def __init__(self, kelvin):
#         self.kelvin = kelvin
        
#     def get_kelvin(self):
#         return self.kelvin
    
#     def set_kelvin(self, kelvin ):
#         self.kelvin = kelvin    
        
#     @staticmethod
#     def kelvin_to_Celsius(kelvin):
#         return kelvin - 273.15
    
#     @staticmethod
#     def kelvin_to_fahrenheit(kelvin):
#         return kelvin * 9/5 - 459.67
    
#     def __str__(self):
#         return f'{self.kelvin} K'
    
# temp = Temperature(100)
# pritn(f'{temp.get_kelvin()} K is equal to {Temperature.kelvin_to_celsius(temp.get_kelvin())} C')
# pritn(f'{temp.get_kelvin()} K is equal to {Temperature.kelvin_to_fahrenheit(temp.get_kelvin())} F')

# Task Nr.2:
# Create a class that would take at least five imperial system measurements and would transform with the help \
    # of static methods to metric system units.

# class ImperialToMetric:
#     @staticmethod
#     def inch_to_cm(inch):
#         return inch * 2.5
    
#     @staticmethod
#     def foot_to_mm(foot):
#         return foot * 0.30
    
#     @staticmethod
#     def yard_to_m(yard):
#         return yard * 0.91
        
#     @staticmethod
#     def mile_to_km(mile):
#         return mile * 1.6
    
#     @staticmethod
#     def pound_to_kg(pound):
#         return pound * 0.45
    
# imperial = ImperialToMetric()
# print(imperial.inch_to_cm(10)) #25.0
# print(imperial.foot_to_mm(5)) #1.5
# print(imperial.yard_to_m(2)) #1.82
# print(imperial.mile_to_km(10)) #16.0
# print(imperial.pound_to_kg(100)) #45.0




    
    

