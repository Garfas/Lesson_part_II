#2023.03.22
# from typing import Optional


# from pydantic import BaseSettings,  IPvAnyAddress

# class Settings(BaseSettings):
#     MONGODB_URL: IPvAnyAddress
#     API_V1_STR: str = "/api/v1"
#     GF_API_URL: Optional[str] = None
#     TOKEN_SECRET_KEY: str ="fj0823t8y3t9shoidn9184h13iudhaslidfuh3190841-00=52394hfu"
    
# settings = Settings()

# print(settings.MONGODB_URL)





# Task Nr.1
# write a function that accepts a number as a parameter. The function should return a number that’s the difference between the largest and smallest numbers that the digits can form in the number.
# For example, if the parameter is “213”, the function should return “198”, which is the result of 123 subtracted from 321.
import sys
def find_difference(num):
    digits = list(str(num))
    sorted_digits =sorted(digits)
    smallest_num = int("".join(sorted_digits))
    reversed_digits = sorted(digits, reverse=True)
    largest_num = int("".join(reversed_digits))

    # print("Smallest number:", smallest_num)
    # print("Largest number:", largest_num)

    return largest_num - smallest_num

difference = find_difference(213)
print("Difference:", difference)

# Task Nr.2
#write a function that accepts an encoded string as a parameter. This string will contain a first name, last name, and an id.
# Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros. The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.
# An example input would be “Robert000Smith000123”. The function should return the following using that input:
# { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }