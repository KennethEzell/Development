'''
You work for a transportation company and need to create a program to manage their fleet of vehicles. Use class inheritance to create a hierarchy of vehicle classes.
First, create a base class called Vehicle that has these attributes and methods.
Attributes: make: string, model: string, year: int
Methods:
__str__() which returns a string in the format "[year] [make] [model]"
get_age() which returns how old the vehicle is, given its year
 
Create a subclass called Car that inherits from Vehicle and adds:
Attribute: num_doors: int
Method: person_space(), which returns the number of people that can fit in the car as num_doors*1.3, truncated to the nearest integer.
 
Create a subclass called SUV that inherits from Car and adds:
Attribute: cargo_space: int
Method: cargo_person_ratio(), which returns the ratio of cargo space to people as cargo_space/person_space()
 
'''

from datetime import datetime
import math


class Vehicle(object):
    ''' This would be my documentation '''
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year


    def __str__(self) -> str:
        return f'{self.year} {self.make} {self.model}'
    
    def get_age(self):
        print(f'Vehicle Age: {datetime.now().year - self.year}')

# this will be a subclass of vehicle 

'''Documentation for class'''
class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, num_doors: int):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def person_space(self):
        return math.trunc(self.num_doors * 1.3)
    
class suv(Car):
    ''''''
    def __init__(self, make: str, model: str, year: int, num_doors: int, cargo_space: int):
        super().__init__(make, model, year, num_doors)
        self.cargo_space = cargo_space

    def cargo_person_ratio(self):
        return f'Cargo to person ratio: {self.cargo_space / self.person_space()}'       
        
       

        