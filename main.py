# Cafeteria project : Create an live menu and payment system (a.k.a console program) :
# First the program should ask if table was reserved/ not (Providing your full name) . And then if not would assign you a table 
# (there is a specific number single, double or family tables) . After table is assigned to you, system should show how many free 
# tables are and how which are reserved/occupied. The system must be able to show name/surname of the person of the reserved table 
# (CLI option : enter reserved table nuber ; OUTCOME: Name/Surname/Time Reserved)
# After assigning table, system should show different menu options for breakfast, lunch , dinner , drinks 
# (alcohol. alcohol free), to choose from. Special menu for vegetarian and vegan must be included too in the special menu.
# All menu items should have weight, preparation time in minutes, calories, and price.
# I have to have an option to change the order before the payment section. Thus I can delete, add more, update amount of the same order.
# I should be able to choose whatever I want from all menus in one ordering. After I finish, I need to see what I chosen, 
# the full payable amount and approx waiting time for the food to be served
# Add an option to add tips (% from the full cost) to the final bill.
# After the payment , system should generate the receipt (logging).



import datetime
import logging

class table:
    def _init (self, number, seats):
        self.number = number
        self.seats = seats
        self.reserved = False
        self.reservation = None
   
        
class Reservation:
    def __init__(self, name, phone, num_guests, time, date):
        self.name = name
        self.phone = phone
        self.num_guests = num_guests
        self.time = time
        self.date =date
        

class Menu:
    def __init__(self) -> None:
        self.menu:dict= {}
           
    def add_breakfast_item(self, name, weight, preparation_time, calories, price, vegetarian=False):
        if "breakfast" not in self.menu:
            self.menu["breakfast"] = [
                {"name": "Eggs Benedict", "weight": 300, "prep_time": 15, "calories": 500, "price": 20},
                {"name": "Pancakes", "weight": 200, "prep_time": 10, "calories": 400, "price": 15}  
            
            ]
        self.menu["breakfast"].append({"name": name, "weight": weight, "prep_time": preparation_time, "calories": calories, "price": price, "vegetarian": vegetarian})

    def add_lunch_item(self, name, weight, preparation_time, calories, price, vegetarian=False):
        if "lunch" not in self.menu:
            self.menu["lunch"] = [
                {"name": "Caesar Salad", "weight": 250, "prep_time": 5, "calories": 300, "price": 12},
                {"name": "Burger", "weight": 350, "prep_time": 15, "calories": 800, "price": 18}  
            
            ]
        self.menu["lunch"].append({"name": name, "weight": weight, "prep_time": preparation_time, "calories": calories, "price": price, "vegetarian": vegetarian})

    def add_dinner_item(self, name, weight, preparation_time, calories, price, vegetarian=False):
        if "dinner" not in self.menu:
            self.menu["dinner"] = [
                {"name": "Grilled Salmon", "weight": 300, "prep_time": 20, "calories": 450, "price": 25},
                {"name": "Steak", "weight": 400, "prep_time": 25, "calories": 1000, "price": 30},
                
            ]
        self.menu["dinner"].append({"name": name, "weight": weight, "prep_time": preparation_time, "calories": calories, "price": price, "vegetarian": vegetarian})
    
    def add_drink_item(self, name, weight, preparation_time, calories, price, vegetarian=False):
        if "drinks" not in self.menu:
            self.menu["drinks"] = [
                {"name": "Coca cola", "weight": 250, "prep_time": 2, "calories": 250, "price": 2},
                {"name": "Water", "weight": 250, "prep_time": 2, "calories": 0, "price": 1},
                
            ]
        self.menu["drinks"].append({"name": name, "weight": weight, "prep_time": preparation_time, "calories": calories, "price": price, "vegetarian": vegetarian})
        
        
class Payment:
    def __init__(self):
        self.reservation = Reservation
        
    def select_payment_method(self):
        if self.reservation.table.reserved:
            print("Please select a payment method:")
            print("1", "Cash")
            print("2", "Bank card")
            choice = input("Enter your payment method (Cash, Bank)")
            if choice == "Cash":
                print("Payment received in cash.")
                logging.info("Payment received in cash:{}".format(self.reservation.table.reserved))
            elif choice == "Bank card":
                print("Payment received by bank card.")
                logging.info("Payment received by bank card:{}".format(self.reservation.table.reserved))
            self.reservation.table.reserved = False
            self.reservation.table.reservation = None
            print("Reservation cancelled.")
            logging.warning("Reservation canceled after payment::{}".format(self.reservation.table))
        else:
            print("No reservation found.")
            logging.info("No reservation found for payment::{}".format(self.reservation.table))
            
logging.info(filename='restaurant.log', level=logging.INFO)

class Restaurant:
    def __init__(self) -> None:
        
            
            
            
            
# def main():
#     restaurant = Restaurant()
#     while True:
#         print ("Welcome to the restaurant")
#         print("Please select an optinion")
#         print("1. View tables")
#         print("2. Make a new reservation")
#         print("3. Cencel a reservation")
#         print("4. Make a peyment")
#         print("5. View menu")
#         print("0. Exit")
        
#         choices = input("Enter your choice: ")
        
#         if choices == "1":
#             restaurant.view_table()
#         elif choices == "2":
#             reservation = reservation.view_table()
#             restaurant.make_reservation(reservation)
#         elif choices == "3":
#             table_number = input("Enter the table number to cancel the reservation ")
#             restaurant.cencel_reservation(int(table_number))
#         elif choices == "4":
#             table_number = input("Enter the table number to make the payment ")
#             restaurant.make_payment(int(table_number))
#         elif choices == "5":
#             restaurant.view_menu()
#         elif choices == "0":
#             break
#         else:
#             print("Invalid choice. Pleas try again")
            
# if __name__ == "__main__":
#     main()
            