# 2023.04.11
#
# 
# 
# Datetime
#Dabartinė data ir laikas:
# import datetime

# x = datetime.datetime.today()
# print(x)
# print(type(x))
# # 2020-11-25 12:41:47.651313

#Tik data:
# x = datetime.date.today()
# print(x)
# print(type(x))


#Tik laikas:
# import datetime
# y = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(y)
# # 2020-02-29 18:20:50

# print(y.strftime("%A, %d. %B %Y %I:%M%p"))
# # Saturday, 29. February 2020 06:20PM


#Laikas su lietuviškumu:
# import datetime
# import locale

# locale.setlocale(locale.LC_TIME, 'lt_LT.UTF-8')
# x = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(x.strftime("%A, %d. %B %Y %I:%M%p"))



# Kaip pridėti ar atimti laiką:
# import datetime

# now = datetime.datetime.now()
# print(now)
# print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=5))
# print(now + datetime.timedelta(days=20, hours=8))

# 2020-11-25 12:26:14.575023
# 2020-11-20 12:26:14.575023
# 2020-11-25 17:26:14.575023
# 2020-12-15 20:26:14.575023


# Kaip sužinoti datų skirtumą (pvz. dienomis):
# import datetime
# now = datetime.datetime.now()
# nepriklausomybes_diena = datetime.datetime(1990, 3, 11)
# skirtumas = now - nepriklausomybes_diena
# print(skirtumas.days)

# 10590

# Kaip įvesti datą/laiką:
# import datetime
# ivesta_data = input("Įveskite datą: ")
# data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
# skirtumas = (datetime.datetime.now() - data)
# print(skirtumas.days)

# Įveskite datą: 2004-03-29 00:00:00
# 5604




# Naudodami timedelta galime pamatuoti, per kiek laiko mūsų kompiuteris susidorojo su užduotimi, pvz.:
# import datetime

# pradzia = datetime.datetime.today()
# for x in range(10000):
#     print("Labas")

# pabaiga = datetime.datetime.today()
# print(f"Programa užtruko {(pabaiga - pradzia).total_seconds()}")




# Taip pat galime į kodą įdėti pauzę:
# import time

# for x in range(10000):
#     print("Labas")
#     time.sleep(2)

# Task Nr.1
#Write a function that calculates difference in days between two datetimes. 

# from datetime import datetime

# def diff_in_days(start_date, end_date):
#     """Calculates the difference in days between two datetime objects."""
#     diff = end_date - start_date
    
#     diff_in_days = diff.days
#     return diff_in_days

# start_date = datetime(2001, 1, 30, 12, 0, 0)
# end_date = datetime (2022, 4, 11, 12, 0, 0)

# diff = diff_in_days(start_date, end_date)
# print("The difference in days is:", diff)


# Write a function that takes a datetime object, which will represent employees starting work day. \
    # and will return amount of total holidays gained during the work until today. 1 Month = 1.6 day off

# import datetime

# def total_holidays_gained(start_date):
#     today = datetime.date.today()
#     months_worked = (today.year - start_date.year) * 12 + (today.month - start_date.month)
    
#     holidays_gained = round(months_worked * 1.6, 1)
    
#     return holidays_gained

# start_date = datetime.date(2020, 1, 1)

# total_holidays = total_holidays_gained(start_date)

# print(total_holidays)#62.4



# find next 3 Fridays that happend to be Friday the 13th (classic)
# import datetime

# def find_next_friday_13th():
#     friday_13th_count = 0
#     current_date = datetime.date.today()
    
#     while friday_13th_count < 3:
#         current_date += datetime.timedelta(days=1)
#         if current_date.day == 13 and current_date.weekday() == 4:
#             friday_13th_count += 1
#             print(current_date)
            
# find_next_friday_13th()


# Write a python function that takes nothing but returns the datetime object of last Friday
# import datetime
# def last_friday():
#     today = datetime.datetime.today()
#     offset = today.weekday() - 4 % 7
#     last_friday = today - datetime.timedelta(days=offset)
#     return datetime.datetime.combine(last_friday, datetime.time.min)

# print(last_friday())







# # Write a Python program to get the last day of a specified year and month, Example: Monday, Tuesday etc.
# import datetime

# def last_day(year, month):
#     last_day = datetime.date(year, month, 1)
#     last_day = last_day.replace(day = 28)
#     while True:
#         try:
#             last_day = last_day.replace(day = last_day.day + 1)
#         except ValueError:
#             break
#     return last_day.strftime("%A")

# print(last_day(2023, 12))


# Write a terminal program that required user to login. If user does not have an account he should register. credentials are username and password. Store the information in the file txt or pickle. Validate user credentials from the file. Once user has logged in: print text: "Hello, <username>"