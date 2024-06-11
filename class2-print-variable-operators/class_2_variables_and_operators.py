# Let's talk about the print statement
# I am a comment

# print('Hello World') # Print built in function




# Addition
# print(4 + 2)
# print (7 +10)
# print(100 + 200)

# Subtraction


# print(10 - 7)
# print(4 - 3)
# print(9 - 8)

# Multiplication

# print(4 * 8)
# print(3 * 9)
# print(11 * 9)

# Division

# print(10 / 2)
# print(5 / 0)

# Try Except

# try:
#     print(5/0)
# except ZeroDivisionError as e:
#     print("You cannot divide by 0")

# Exponents
# print(5 ** 5)
# print(2 ** 5)
# print(3 ** 6)

# Integer Division

# print(10 // 3)
# print(4 // 3)
# print(5 // 2)

# Modulo / Mod / Remainder

# print(5 % 2)
# print(10 % 4)

# Using variable as placeholders
# This is assigning integer value 1 to vaiable num_one


num_one = 1
num_two = 20

# print(num_one)
# print(num_one + num_two)

# Program to find the perimeter of a rectable
# perimenter = 2 * (length + width)

# declariong your variable
length = 10
width = 7

# perimeter = 2 * (length +width)

# print(perimeter,length,width)

# print('The perimeter of my rectangle is',perimeter)


# Data Typeas

# Integer
num_3 = 5 # declare variable

# print(num_3) # print variable value
# print(type(num_3)) # we can check data type

# Strings
fav_color = 'blue'
# print(fav_color)
# print(type(fav_color))

# Boolean
technical_errors = True
# print(technical_errors)
# print(type(technical_errors))

# Float

num_4 = 4.05
# print (num_4)
# print(type(num_4))

# List
students_grades =[100, 95, 70, 85, 40]
# print(students_grades)
# print (type(students_grades))

# For loop
# for s in students_grades: # s is a temporary variable for each student grade in the list
#     print('One grade is', s)

# Dictionaries
demographic_info = {"First name":'Joe',
                    "Last name": 'Smith',
                    "State": 'NY'}

# print(demographic_info)
# print(type(demographic_info))

# Casting - changing the data type of a value.   
# When you get input from a user Python will make it a string
my_string = '5'
# print(my_string)
# print(type(my_string))

new_number = int(my_string) # casting our string 5 to a integer
# print(new_number)
# print(type(new_number))


# Cast Integer to a astring

second_num = 10
# print (type(second_num))

new_string = str(second_num)
# print(type(new_string))

# Colors
my_fav_colors = ['blue', 'black', 'purple', 'green']
len_counts_the_items = len(my_fav_colors) # we are passing the argument mycount
# print(what_am_i_doing)

one_color = 'orange'
# my_count = len(one_color)
# print(my_count)

# for o in one_color:
#     print(o)TWOL

# Eval
cold_weather = 'True'
# print(eval(cold_weather))

# find the perimeter of a triangle 
# perimenter = side_one + base + Side_two
# User has a triangle with one side (6), one side (7), base (4)

side_one = 6
side_two = 7
base = 4

perimenter = (side_one + side_two + base)
print(perimenter)
 
