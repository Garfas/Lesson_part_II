# 2023 03 27
# OOP Advanced [lesson4]: Method chaining & super function.


class MyString:
    def __init__(self, value: str):
        self.value = value  
          
        def add_exclamation(self) -> 'MyString':
            self.value += "!"        
            return self    
    
    def make_upper(self) -> 'MyString':
        self.value = self.value.upper()
        return self    
    
    def get_self_value(self) -> str:
        return self.value

my_string = MyString("Antanas")
my_string.add_exclamation().make_upper()

print(my_string.value) # output: "HELLO!"print(my_string.get_self_value())
print(my_string.get_self_value())


class Rocket:
    def __init__(self):
        self.name = None        
        self.speed = None    
        
    def give_name_condition_a(self, name: str) -> 'Rocket':
        self.name = name + 'whateber'        
        return self    
    
    def give_name_condition_b(self, name: str) -> 'Rocket':
        self.name = name + 'Antoska'        
        return self    
    
    def update_speed(self, speed: float) -> 'Rocket':
        self.speed = speed        
        return self    
    
    def get_rocket_values(self) -> Tuple[str, float]:
        return self.name, self.speed
    
my_rocket = Rocket()

my_rocket.give_name('Nasa').update_speed(250.36)

print(f'My Rocket params: name {my_rocket.name} and speed {my_rocket.speed}')



# Task Nr.1:
# Create a class Person that has two methods: set_name and set_age, which set the name and age attributes of the class, respectively. 
# Modify these methods to return self, so that the calls can be chained together.