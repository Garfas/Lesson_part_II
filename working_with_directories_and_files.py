# 2023 04 05
# Darbas su katalogais ir failais


import os
from datetime import datetime

# os.chdir('C:\\Users\\Donoras\\Desktop')
# print(os.getcwd())

# print(os.getcwd()) 

# os.mkdir("new_folder") #sukuria aplanką toje vietoje kur dirbam

# print(os.listdir()) #Kaip pažiūrėti, kokie failai ir katalogai yra kataloge:

# os.makedirs("Naujas_katalogas/Katalogakataloge") #Kaip sukurti naują katalogą:
# print(os.listdir())


# print(os.stat("working_with_directories_and_files.py "))#Kaip sužinoti failo/katalogo informaciją:
# print(os.stat("working_with_directories_and_files.py "))


# print(os.stat("working_with_directories_and_files.py ").st_size)#Kaip sužinoti failo dydį:


# print(os.stat("working_with_directories_and_files.py").st_mtime)#Kaip sužinoti kada failas buvo paskutinį kartą modifikuotas:

# from datetime import datetime
# data = os.stat("working_with_directories_and_files.py").st_mtime
# print(datetime.fromtimestamp(data)) #Pakeitus suprantamu formatu kada failas buvo paskutinį kartą modifikuotas:



#Tekstinių failų kūrimas ir nuskaitymas
#sukurai txt dokumentą
# with open("file.txt", 'w') as f:
#     f.write("Sveikas, pasauli!")

# file = open ("file.txt", 'w') geriaU nenaudot
# file.write("Sveikas, pasauli!")
# file.close()



# #Kaip įrašyti ir nuskaityti failą vienu metu:
# with open("failas.txt", 'r+') as failas:
#     print(failas.read())
#     failas.write("Labas rytas, pasauli!")

# # Sveikas, pasauli!
# with open("failas.txt", 'r') as failas:
#     print(failas.read())#Sveikas, pasauli!Labas rytas, pasauli!


# with open("failas.txt", 'w', encoding="utf-8") as failas:
#     failas.write("Čia yra pirmas sakinys \n")

# with open("failas.txt", 'a', encoding="utf-8") as failas:
#     failas.write("Čia yra antras sakinys \n")


#Kaip perrašyti tekstą norimoje vietoje:
# with open("failas.txt", 'w', encoding="utf-8") as failas:
#     failas.write("Test")
#     failas.write("Test")



# #Kaip perrašyti tekstą norimoje vietoje:
# with open("failas.txt", 'w', encoding="utf-8") as failas:
#     failas.write("Test")
#     failas.write("Test")
    
# with open("failas.txt", 'w', encoding="utf-8") as failas:
#     failas.write("Test")
#     failas.seek(0)
#     failas.write("BE")


# #Darbas su dviem failais (teksto kopijavimas iš vieno į kitą):
# with open("failas.txt", 'r', un) as r_failas:
#     with open("failo_kopija.txt", 'w') as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)

#Dvejetainių failų kopijavimas:
#problema
# with open("logo.png", 'r') as r_failas:
#     with open("logo_kopija.png", 'w') as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 65: character maps to <undefined>

#Sprendimas:
# with open("pictures.jpg", 'rb') as r_failas:
#     with open("pictures_copy.jpg", 'wb') as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)
            
            
            
            
#Kaip į failą išsaugoti kintamuosius/objektus
#(modulis pickle)

#Įrašymas:
import pickle

# a = 1024

# with open("a.pkl", "wb") as pickle_out: #pkl yra pickle failas
#     pickle.dump(a, pickle_out)
    
# #Nuskaitymas:    
#     import pickle

# with open("a.pkl", "rb") as pickle_in:
#     naujas_a = pickle.load(pickle_in)

# print(naujas_a) #1024


#Išsaugome masyvą:

# import pickle

# zodynas = {1:"Pirmas", 2:"Antras", 3:"Trečias"}

# with open("zodynas.pkl", "wb") as pickle_out:
#     pickle.dump(zodynas, pickle_out)
    
# #Nuskaitymas:
# import pickle

# with open("zodynas.pkl", "rb") as pickle_in:
#     naujas_zodynas = pickle.load(pickle_in)

# print(naujas_zodynas)# {1: 'Pirmas', 2: 'Antras', 3: 'Trečias'}


# Task nr.1
# Sukurti programą, kuri:
# Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
# Atspausdintų tekstą iš sukurto failo
# Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
# Atspausdintų visą failo tekstą atbulai
# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS

import os
from datetime import datetime

#A text.txt file would be created with the full text obtained by running "import this" in the python code
import this
with open("Text.txt", "w") as f:
    f.write(this.s)
    
#print this text from the created file 
with open("Text.txt", "r") as f:
    print(f.read())
#It would add today's date and time to the last line of the created file    
with open("Text.txt", "a") as f:
    now = datetime.today()
    f.write(f"\nLast updated on: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
#Numbered lines of text (a number added at the beginning of each)
with open("Text.txt", "r") as f:
    lines = f.readlines()
    with open("Numbered_Text.txt", "w") as f2:
     for i, line in enumerate(lines):
         f2.write(f"{i+1}.{line}")

#In the created file, the line "Beautiful is better than ugly." would change to "Gražu yra geriau nei bjauru."
with open ("Text.txt", "r") as f:
    lines = f.readlines()
    with open("Update_Text.txt", "w", encoding="utf8") as f2:
        for line in lines:
            if "Beautiful is better than ugly." in line:
                f2.write("Gražu yra geriau nei bjauru.\n")
            else:
                f2.write(line)

# Would print the entire text of the file in reverse
with open("Text.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[::-1]))
    
# print the number of words, numbers, uppercase and lowercase letters in the text of the file
with open("Text.txt", "r") as f:
    text = f.read()
    words = len(text.split())  
    numbers = sum(c.isdigit() for c in text)
    uppercase = sum(c.isupper() for c in text)
    lowercase = sum(c.islower() for c in text)
    print(f"Words: {words} \nNumbers: {numbers} \nUppercase: {uppercase} \nLowercase: {lowercase}")  

# Copy all the text of the created file to a new file, in CAPITAL LETTERS only
with open("Text.txt", "r") as f:
    text = f.read()
    with open ("UPPERCASE_Text.txt", "w") as f2:
        f2.write(text.upper())
              
    
    

