# Create a Person class which will have three properties:
#      In the house
#      List of foods they like
#      List of foods they hate
# In this class, create the method taste():
#      It will take in a food name as a string.
#      Return {person_name} eats the {food_name}.
#      If the food is in the person's like list, add 'and loves it!' to the end.
#      If it is in the person's hate list, add 'and hates it!' to the end.
#      If it is in neither list, simply add an exclamation mark to the end.
#      p1 = Person("Sam", ["ice cream"], ["carrots"])
#      p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
#      p1.taste("cheese") ➞ "Sam eats the cheese!"
#      p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

from typing import List

class Person:
    def __init__(self, name : str, likes : List[str], hates : List[str]):
        self.name = name
        self.likes = likes
        self.hates = hates


    def taste(self, food : str) -> str:
        if food in self.likes:
            return f'{self.name} eats the {food} and loves it.'
        
        elif food in self.hates:
            return f'{self.name} eats the {food} and hates it !'
        
        else:
            return f'{self.name} eats the {food} !'

p1 = Person('Sam', ['ice cream'], ['carrot'])

print(p1.taste('ice cream'))
print(p1.taste('cheese'))
print(p1.taste('carrots'))
            
#////////////////////////////////

# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.
#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
# Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented.


# from typing import List


class Smoothie:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self) -> float:
        cost = 0
        for ingredient in self.ingredients:
            cost += ingredient["cost"]
        return cost
    

    def get_price(self) -> float:
        cost = self.get_cost()
        price = cost + (cost * 1.5)
        
        return round(price, 2)
    
    def get_name(self) -> str:
        ingredient_list = [ingredient["name"].replace("berries" , "berry") for ingredient in self.ingredients]
        ingredient_list.sort()
        if len(ingredient_list) > 1:
            name = " ".join(ingredient_list) + "Fusion Smothie"
        else:
            name = ingredient_list[0] + "Smoothie"
        return name
        

class BananaBerrySmoothie(Smoothie):
    def __init__(self) -> None:
        ingredients = [
            {"name" : "banana", "cost" : 0.5},
            {"name" : "strawberries-berries", "cost" : 0.75},
            {"name" : "blueberies-berries", "cost" : 0.65},
            {"name" : "yogurt", "cost" : 1.5},
            {"name" : "honey", "cost" : 0.25}
        ]
        super().__init__(ingredients)


class MangoPinapleSmoothie(Smoothie):
    def __init__(self) -> None:
        ingredients = [
            {"name" : "mango", "cost" : 1.0},
            {"name" : "pineaple", "cost" : 0.45},
            {"name" : "orange-juice", "cost" : 1.45},
            {"name" : "ice", "cost" : 0.1}
        ]
        super().__init__(ingredients)


s1 = BananaBerrySmoothie()

print(s1.get_name())
print(s1.get_cost())
print(s1.get_price())

s2 = MangoPinapleSmoothie()
print(s2.get_name())
print(s2.get_cost())
print(s2.get_price())

#/////////////////////////////
# Create a class Sudoku that takes a string as an argument. The string will contain the numbers of a regular 9x9 sudoku board left to right and top to bottom, with zeros filling up the empty cells.
# Attributes
# An instance of the class Sudoku will have one attribute:
#     board: a list representing the board, with sublits for each row, with the numbers as integers. Empty cell represented with 0.
# Methods
# An instance of the class Sudoku wil have three methods:
#     get_row(n): will return the row in position n.
#     get_col(n): will return the column in position n.
#     get_sqr([n, m]): will return the square in position n if only one argument is given, and the square to which the cell in position (n, m) belongs to if two arguments are given.
#     game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
# game.board ➞ [
#   [4, 1, 7, 9, 5, 0, 0, 3, 0],
#   [0, 0, 0, 0, 0, 0, 7, 0, 0],
#   [0, 6, 0, 0, 0, 7, 0, 0, 0],
#   [0, 5, 0, 0, 0, 9, 1, 0, 6],
#   [8, 0, 0, 6, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 3, 4, 0, 0],
#   [9, 0, 0, 0, 0, 5, 0, 0, 0],
#   [0, 0, 0, 4, 3, 0, 0, 0, 0],
#   [2, 0, 0, 7, 0, 1, 5, 8, 0]
# ]
# game.get_row(0) ➞ [4, 1, 7, 9, 5, 0, 0, 3, 0]
# game.get_col(8) ➞ [0, 0, 0, 6, 0, 0, 0, 0, 0]
# game.get_sqr(1) ➞ [9, 5, 0, 0, 0, 0, 0, 0, 7]
# game.get_sqr(1, 8) ➞ [0, 3, 0, 7, 0, 0, 0, 0, 0]
# game.get_sqr(8, 3) ➞ [0, 0, 5, 4, 3, 0, 7, 0, 1]