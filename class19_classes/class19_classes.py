import datetime
from datetime import dateti

''' classes'''

class Point2d():
    # This first method, is your constructor it builds your object
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    # This is our string method, it delivers a string representation
    def __str__(self):
        return f'({self.x},{self.y})'
   
    # This will control the == operator
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
   
    def __add__(self, other):
        return Point2d(self.x + other.x, self.y + other.y)
   
    def __sub__(self, other):
        return Point2d(self.x - other.x, self.y - other.y)
    
    def __sub__(self, other):
        return Point2d(self.x - other.x, self.y - other.y)
   
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False

    # mutator method
    def set_x(self, new_x):
        self.x = new_x
    
    def set_y(self, new_y):  # Mutator method
	    self.y = new_y


   
point1 = Point2d(3, 5) # created an object of the class
point2 = Point2d(4, 11)

point3 = point1 + point2
point4 = Point2d(10, 11)
point5 = point4 - point3

jeans_point = Point2d(5, 11)
jeans_point.set_x(25)
jeans_point.set_y(15)
print(jeans_point)

# my_x_value = jeans_point.get_x()
# my_y_value = jeans_point.get_y()

 
'''  Date Class '''
class Date:

    def __injit__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.month:02d}/{self.day:02d}/{self.year}'
    
    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False
    
    def __lt__(self, other):
        selfdate = datetime(self.year, self.month, self.day)
        otherdate = datetime(other.year, other.month, other.day)
        if selfdate < otherdate:
            return True
        return False
    
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        """Return True if the year is a leap year, False otherwise."""
        year = self.year
        if (year % 4 == 0):
            if (year % 100 != 0) or (year % 400 == 0):
                return True
        return False    




first_date = Date(2000, 10, 4)
second_date = Date(1985, 5, 10)

    
my_date_info = Date(2004, 10, 4)
print(my_date_info)


# print(point1)
# print(point2)
 
# # __eq__
# print(point1 == point2)
 
# #__add__
# point3 = point1 + point2
# print(point3)

# class Point2d():
# # this first method is the constructor it builds your objeck
#     def ___init__(self, x, y) :
#         self.x = x
#         self.y = y

# # this is our string method, it delivers a string representation
#     def __str__(self):
#         return f'(your first parameter is {self.x}, your second parameter is {self.y})'
    
# # this will control the == operator
#     def __ea__(self, other):
#         if self.x == other.x and self.y == other.y:
#             return True
#         return False
    
#     def __add__(self, other):
#         return Point2d(3, 10)



# point1 = Point2d(3, 5)    
# point2 = Point2d(3, 2)
# # print(point1)
# # print(point2)

# print(point1 == point2)

# point3 = point1 + point2
# print(point3)