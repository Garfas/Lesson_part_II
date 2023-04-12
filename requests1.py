# # 2023 04 04


# # get
# # put
# # post
# # delete


# # import requests
# # response = requests.get('http://google.com')
# # print(response.status_code)


# # r = requests.get('http://python.org/blabla')
# # if r.status_code not in range(400, 600):
# #     print('Pavyko prisijungti! Dirbame toliau...')
# # else:
# #     print(f'Kažkas ne taip.. Kodas {r.status_code}')
# # # Kažkas ne taip.. Kodas 404


# # r = requests.get('http://python.org/blabla')
# # if r.ok:
# #     print('važiuojam toliau!')
# # else:
# #     print(f'Klaida! kodas {r.status_code}')
# # # Klaida! kodas 404


# # r = requests.get('https://httpbin.org/ip')
# # print(r.text)


# # payload = {'q': 'pep', 'page': 2 }
# # r = requests.get('https://www.google/search?', params=payload)
# # print(r.status_code)


# # data = {'name': 'Jonas', 'lastname': 'Jonaitis'}
# # r = requests.post('http://httpbin.org/post', data=data)
# # print(r.text)
# # # ... 
# # # "form": {
# # #     "lastname": "Jonaitis", 
# # #     "name": "Jonas"
# # #   }, 
# # #  ...



# import json

# data = '''{
#   "student": [ 

#      { 
#         "id":"01", 
#         "name": "Tom", 
#         "lastname": "Price" 
#      }, 

#      { 
#         "id":"02", 
#         "name": "Nick", 
#         "lastname": "Thameson" 
#      } 
#   ]   
# }'''

# data_dict = json.loads(data)
# print(data_dict)
# print(type(data_dict))

# data_dict['student'][1]['name'] = 'Kyle'
# for student in data_dict['student']:
#     student.update({'gender':'male'})
# print(data_dict)

# # {'student': [{'id': '01', 'name': 'Tom', 'lastname': 'Price', 'gender': 'male'}, 
# # {'id': '02', 'name': 'Kyle', 'lastname': 'Thameson', 'gender': 'male'}]}


#Task Nr.1
 #parašykite programą, kuri nuskaitys failo turinį ir performuos jį taip:
 #Išsaugokite rezultatą į .json failą savo kompiuteryje.

# import json

# #read file contents
# with open('Task_nr1.txt', 'r') as file:
#     contents = file.read()
    
# #split contents into lines
# lines = contents.split('\n')

# #create list of colors objects
# colors = []
# for line in lines:
#     if line:
#         values = line.split(',')
#         color_object = {
#             "color": values[0].strip(),
#             "category": values[1].strip(),
#             "type": values[2].strip(),
#             "code":{
#                 "rgba":[int(v) for v in values[3].split()],
#                 "hex": values[4].strip()
#             }
#         }
#         colors.append(color_object)

# #create JSON object
# json_object = {
#     "colors": colors
# }


# #write to output file
# with open(Task_answer.json, 'w') as file: #WTF??????????
#     json.dump(json_object, file, indent=2)
  
  
  
    
    
# Task Nr.2
# https://cataas.com/cat kas kartą užkrauna vis skirtingą katės nuotrauką. 
# Parašykite funkciją, kuriai į parametrus įrašius, kiek norime nuotraukų, išsaugotų jas mūsų kompiuteryje.

# import requests







# Task Nr.3
# parašykite funkciją, kuri į args priimtų url eilučių sąrašą ir grąžintų, kokį serverį naudoja svetainė. 
# Atsakymas galėtų atrodyti maždaug taip:
# URL                     Server
# -------------------------------------
# https://www.delfi.lt/   DWS
# https://www.alfa.lt/    nginx/1.10.3 (Ubuntu)
# https://www.15min.lt/   nginx
# https://www.lrytas.lt/  shield
# http://www.google.com/  gws

import requests
from urllib.parse import urlparse

def get_server(urls):
    

# Task nr.4
# Parašykite programą, kuri iš adreso https://orai.15min.lt/prognozes ištrauktų ir atspausdintų oro prognozę Vilniuje šiuo metu. 
# Galima naudoti str metodus, regex.

# import requests
# from bs4 import BeautifulSoup
# import re

# #make a request to the website
# url = "https://www.gismeteo.lt/weather-dovilai-16011/"
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# dovilai_section = soup.find('div', {'class': 'wsection wdata'})

# weather_forecast = dovilai_section.find('div', {'class': 'wsection wdata_item wdata_item_type_condition'}).text.strip()

# print(weather_forecast)