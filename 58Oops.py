# Oops Concept :

# Class and Object : 

class Car():
 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.make} {self.model} {self.year}")

# Create Object ---->
    
my_car1 = Car('BMW', 'iX1', 2023)
my_car2 = Car('Audi', 'A3', 2024)
my_car3 = Car('Kia', 'EV6', 2022)
my_car4 = Car('Toyota', 'GR86', 2020)


my_car1.display_info()     
my_car2.display_info()
my_car3.display_info()
my_car4.display_info()
