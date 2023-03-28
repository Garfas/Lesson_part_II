from abc import ABC, abstractmethod
import datetime
import logging
import time


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class Table(ABC):
    @abstractmethod
    def is_reserved(self):
        pass
    
    @abstractmethod
    def assign_table_number(self):
        pass
    
class RestaurantTable(Table):
    def __init__(self):
        self.table_number = None
        self.is_occupied = False
        self.reserved_by = None
        
        
    def is_reserved(self):
        return self.reserved_by 
    
    def assign_tables_number(self, table_number):
        self.table_number = table_number
        self.is_occupied = True
    tables_numbers = {
        "single": {
            "free": ["1", "2", "3"]}, "reserved": {}
            },
    {
        "double": {
            "free":["4", "5"]}, "reserved": {}
        },
    {
        "family": {
            "free": ["6"], "reserved":{}}
            }
    
    
class Restaurant():
    def __init__(self):
        self.table = []
        self.reversed_tables = []
        self.menu = {
            "breakfast":{
                "menu_items":{
                    "toast":{"weight": 100, "preperation_time": 10, "calories": 130, "price": 5},
                    "pancakes": {"weight": 250, "preperation_time": 15, "calories": 200, "price":7},
                    "croissant": {"weight": 80, "preperation_time": 5, "calories": 180, "price": 3},
                }
            },
            "lunch": {
                "menu_items":{
                    "sandwich": {"weight": 250, "preperation_time": 5, "calories": 400, "price": 6},
                    "burger": {"weight": 200, "preperation_time": 10, "calories": 700, "price": 8},
                    "slad": {"weight": 250, "preperation_time": 10, "calories": 100, "price": 5}
                }
            },
            "dinner":{
                "menu_items":{
                    "pasta": {"weight": 300, "preperation_time": 15, "calories": 500, "price": 9},
                    "steak": {"weight": 300, "preperation_time": 20, "calories": 1000, "price": 15},
                    "grilled fish": {"weight": 300, "preperation_time": 15, "calories": 700, "price": 12}   
                }
            },
            "special": {
                "menu_items": {
                    "vegan salad": {"weight": 220, "preperation_time": 10, "calories": 100, "price": 6},
                    "vegetarian pasta":{"weight": 300, "preperation_time": 15, "calories": 350, "price": 8}
                }
                
            },
            "drinks": {
                "menu_items": {
                    "water": {"weight": 200, "preperation_time": 1, "calories": 0, "price": 0},
                    "juice": {"weight": 250, "preperation_time": 5, "calories": 100, "price": 2},
                    "soda": {"weight": 200, "preperation_time": 2, "calories": 120, "price": 1}
                }
            }
            
        }

        self.total_price = 0
        self.orders = {"orders": []}
        
    def show_menu(self):
        print("Here is the menu:")
        for meal, data in self.menu.items():
            print(f"\n{meal.title()} Menu:")
            for item, details in data["menu_items"].items():
                print(f'{item.title()} ({details["weight"]}g, {details["calories"]}cal) - ${details["price"]}')
                
    def place_order(self):
        print("\nPleas enter your tables number and the items you would like to order.")
        table_number = int(input("Tables Number:"))
        order = input("Order (seperate items with commas):")
        order_items = order.split(",")
        order_items = [item.strip() for item in order_items]
        
        table = self.tables[table_number - 1]
        table.is_occupied = True
        
        for item in order_items:
            if item not in self.menu["breakfest"]["menu_items"] and \
                    item not in self.menu["lunch"]["menu_items"] and \
                    item not in self.menu["dinner"]["menu_items"] and \
                    item not in self.menu["drinks"]["menu_items"] and \
                    item not in self.menu["special"]["menu_items"]:
                print(f"{item} is not in the menu. Please tray again.")
                return
            
        order_time = datetime.datetime.now()
        order_details = {"table_number": table_number, "order_items": order_items, "order_time": order_time}
        self.order['orders'].append(order_details)
        print("Order placed successfully")
        
    def calculate_bil(self):
        print("/")