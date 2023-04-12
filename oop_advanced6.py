# 2023 04 03
# 2023 04 06

# class Calc:
#     MY_NUMBER = 2
#     def __init__(self, nr: int ):
#         self.MY_NUMBER+= nr
        
# calc_one = Calc(nr=3)
# print(calc_one.MY_NUMBER)

# cal_two = Calc(nr=5)
# print(cal_two.MY_NUMBER)



# Task Nr.1:
# Create a class method to return the factorial of a given number.

# class Mathoperations:
    
#     @classmethod
#     def factorial(cls, num: int):   
#         """Calculates the factorial o a given number """
        
#         #base case
#         if num == 0:
#             return 1
        
#         # recursive case
#         else:
#             return num * cls.factorial(num - 1)
        
# print(Mathoperations.factorial(10))


# Task Nr.2:
# Create a class method to return the reversed string of a given string.

# class StringUtils:
    
#     @classmethod
#     def reverse_string(cls, string):
         
#          if len(string) == 0:
#              return string[::-1]
         
#          #recursive case
#          else:
#              return string[-1] + cls.reverse_string (string[:-1])
                                                  
# print(StringUtils.reverse_string("Camaro"))

# Task Nr.3
# Create a class method to return the list of prime numbers up to a given number.




# Task Nr.4 
# Create a class to represent a library system. The library system should have a collection of booksthat can be borrowed by users. Users can register to the 
# library system, borrow books, and return books. The library system should keep track of the books borrowed by users, and the number of available copies of each book.

class LibrarySystem:
    def __init__(self, books):
        self.books = {book: 1 for book in books}
        self.users = {}
        self.borrowed_books = {}
        
    @classmethod
    def create_library(cls):
        books = [
            "Book 1", "Book 2", "Book 3", "Book 4", 
            "Book 5", "Book 6", "Book 7", "Book 8", 
            "Book 9", "Book 10", "Book 11", "Book 12", 
            "Book 13", "Book 14", "Book 15", "Book 16",
            "Book 17", "Book 18", "Book 19", "Book 20"
            ]
        return cls(books)
    
    def register_user(self, user_id, name):
        self.users[user_id] = name
        
    def borrow_books(self, user_id, book_title,):
        if book_title not in self.books:
            raise ValueError("Book not found in library system")
        if book_title not in self.borrowed_books:
            self.borrowed_books[book_title] = [user_id]
        elif len(self.borrow_books[book_title]) >= self.books[book_title]:
            raise ValueError("All copys of book are currently borrowed")
        else:
            self.borrowed_books[book_title].append(user_id)
            
    def return_book(self, user_id, book_title):
        if book_title not in self.books:
            raise ValueError("Book not found in library system")
        if book_title not in self.borrowed_books:
            raise ValueError("Book not currently borrowed by any user")
        if user_id not in self.borrowed_books[book_title]:
            raise ValueError("Book not currently borrowed by user")
        self.borrowed_books[book_title].remove(user_id)
        
    def get_available_books(self):
        available_books = {}
        for book_title in self.books:
            if book_title not in self.borrowed_books:
                available_books[book_title] = self.books[book_title]
            else:
                available_books[book_title] = self.books[book_title] -len(self.borrowed_books[book_title])
        return available_books
    
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    def get_users(self):
        return self.users
    
library_system = LibrarySystem.create_library()

library_system.register_user(1, "Mantas")
library_system.register_user(2, "Daiva")
library_system.register_user(3, "Dorianas")
library_system.register_user(4, "Gabrielius")

library_system.borrow_books(1, "Book 1")
library_system.borrow_books(2, "Book 10")
library_system.borrow_books(3, "Book 6")
library_system.borrow_books(4, "Book 19")

available_books = library_system.get_available_books()
print("Available Books:")
for book_title, num_copies in available_books.items():
    print(f"{book_title}: {num_copies}")

borrowed_books = library_system.get_borrowed_books()
users = library_system.get_users()

        

print("Borrowed books:", borrowed_books)
print("Users:", users)