import math


''' Functions pt 2 completed '''

# Lambda with sort

students = [{"name":"Kim","grade":98},
            {"name":"Joe","grade":65},
            {"name":"Ted","grade":93},
            {"name":"Keisha","grade":80},
            {"name":"Torrie","grade":65},
            {"name":"Simon","grade":78}]

# students_by_name = sorted(students, key = lambda s: s["name"])
# print(students_by_name)

# students_by_grade = sorted(students, key = lambda s: s["grade"], reverse=True)
# print(students_by_grade)

# students_by_name = sorted(students, key= lambda s: s['grade'], reverse=True)

# students_by_age = sorted(students, key= lambda s: s['grade'],)

# print(students_by_name)
# print(students_by_age)


# Let's look at reduce
from functools import reduce


# my_list = [1, 2, 3, 4, 5, 6, 10, 1]
# lets_try_reduce = reduce(lambda a, b: a * b, my_list)


# print(lets_try_reduce)

''' More fun with functions'''


''' 
Write a lambda function that makes a string a title case and apply the function to the list below with a map function
words = ['make', 'us', 'title', 'case']

'''

words = ['make', 'us', 'title', 'case']

# result = map(lambda w : w.title(), words)
# print(list(result))



''' Write a lambda function that will add ten to a list item if that list item is greater than or equal to 50, otherwise it will subtract five

my_numbers = [50, 12, 19, 80, 5, 75]
'''

my_numbers = [50, 12, 19, 80, 5, 75]

# result = map(lambda x: my_numbers + 10 if my_numbers >= 50 else my_numbers - 5)

# lambda n:  n + 10 if n >= 50 else n - 5

# print(result(45))

# def add_if(n):

    # return n + 10 if n >= 50 else n - 5
    # # if n >= 50:
    # #     return n + 10
    # # else:
    # #     return n - 5


    

# print(add_if(54))

# def add_if(n):
#     if n >= 50:
#         return n + 10
#     else:
#         return n - 5

# print(add_if(50))

# result = map(add_if(), my_numbers)
# print(result)
# print(lambda n :my_numbers, lambda n + 10 if n>50 else n -5)


    
# ''' Lambda version of add_if 

# # lambda n:  n + 10 if n >= 50 else n - 5
# '''

# my_numbers = [50, 12, 19, 80, 5, 75, 100, 4]

# result = map(lambda n:  n + 10 if n >= 50 else n - 5, my_numbers)
# print(list(result))





# ''' Write a lambda function and utilize reduce to add all the numbers in this list

# add_me_up = [50, 12, 9, 100, 56, 70]

# '''

# my_list = [1, 2, 3, 4, 5, 6, 10, 1]
# lets_try_reduce = reduce(lambda a, b: a * b, my_list)
add_me_up = [50, 12, 9, 100, 56, 70]

# def add_up(print(reduce(lambda, x, y: x + y, add_me_up())))

# print(reduce(lambda x, y: x + y, add_me_up))  



# print(reduce(lambda x, y: x + y,[50, 12, 9, 100, 56, 70.11] ))





''' Compile time errors / static errors'''
# SyntaxError: unterminated string literal 
# print('Wed') 

# SyntaxError: unterminated string literal
# name = 'John'  

# SyntaxError: '(' was never closed
# print("I hope you have a great day")

# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# if x == 10: 

# SyntaxError: expected ':'
    # if x == 10:


''' Exceptions / Runtime errors'''

''' ValueError '''
# ValueError: could not convert string to float: 'testing'
# print(float("testing")) 

# ValueError: math domain error
# print(math.sqrt(-5)) 

# ValueError: not enough values to unpack (expected 3, got 2)
# fname, lname, middlename = 'fritz', 'lewis',

''' AttributeError '''
# AttributeError: 'int' object has no attribute 'append'
# num = 10
# num.append(5) 


# AttributeError: 'str' object has no attribute 'append'
# str1 = 'hello'
# str1.append('buddy')  

''' NameError '''
# NameError: name 'x' is not defined
# print(x) 

# Name error: name 'c' is not define
# for i in range(c): 
#     print(i)  

''' TypeError '''
#TypeError: can only concatenate str (not "int") to str
# color = 'blue'
# age = 25
# result = color + age 


# TypeError: 'str' object is not callable
car = 'chevy'
# car() 

# TypeError: list indices must be integers or slices, not str
fav_animals = ['dog', 'cat', 'bird']
# index_value = '1'
# print(fav_animals[index_value]) 


# TypeError: 'int' object is not iterable
# for i in 155:
#     print(i) 

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# def add_two(num1, num2):
#     return num1 + num2 


# print(add_two(5, 10))


# Keyboard interruption exception

# i = 2
# while i > 0:
#     i += 1
#     print(i)  # KeyboardInterrupt


# Dividing by zero
# num = 5
# denominator = 0

# result = num / denominator



# Let's prevent this

# numerator = int(input('Please enter your numerator: '))
# denominator = int(input('Please enter your denominator: '))
                  
# try: 
#     quotient = numerator / denominator
#     print('youR QUOTIENT IS ' , quotient)
# except ZeroDivisionError:
#     print("sorry you cannot divide by zero")



# Lets implement a try, except, than test

# userin = input('enter a number:')





'''
Exercise - Handling Invalid User Input
Write a Python program that takes a customer's age as user input and determines whether they're eligible for a senior discount.
Sometimes the age might not be in the correct format. Handle this using try-except, and print a descriptive error message if the age can't be cast to an int.
If the age is greater than or equal to 65, the customer is eligible for the discount. Otherwise, they're not eligible. Print whether the customer is eligible or not.

# '''

# customer_age = int(input("Input your age please: "))

# if customer_age >= 65:
#     print("You are eligible for senior discount.")
# else:
#     print("You are ineligible for senior discount. ")

# try:
#       customer_age = int(input("Input your age please: "))
        
# except ValueError:
#     print('Age must be an integer value')
# else:
#     print('You are elible for discount') if customer_age >= 65 else print("You are ineligible for discount. ")
# finally:
#      print('I run no matter what. ')





# try:
#     customer_age = int(input('enter your age: '))

# except ValueError:
#     print('AGE must be an inter.')

# else:
#     print('eligible for discount') if customer_age>= 65 else print('ineligible for discount')



# With Except / Else
# try:
#     customer_age = int(input('enter your age: '))

# except ValueError:
#     print('AGE must be an inter.')

# else:
#     print('eligible for discount') if customer_age>= 65 else print('ineligible for discount')
# try:
#     customer_age>= 65
    # print('eligible for discount')


# With Except / Else / Finally
# try:
#     customer_age = int(input('enter your age: '))

# except ValueError:
#     print('AGE must be an inter.')

# else:
#     print('eligible for discount') if customer_age>= 65 else print('ineligible for discount')

# finally:
#     print('hello, i run no matter what')



''' Exercise 

You can add a finally block that will be executed regardless if the try block raises an error. 
This is good for cleaning up resources, because it will always be run.

'''
# def append_user_input(lis):
#     try:
#         lis.append(float(input("Enter a number: ")))
#     except ValueError:
#         print('Invalid input')
#         return None
#     finally:
#         print("Your list", lis)

# lis = []
# append_user_input(lis)




# lis = []

# def append_user_input(lis):
#     try:
#         lis.append(float(input('enter a number: ')))
        
#     except ValueError:
#         print('invalid input')
#         return None
#     finally:
#         print('your list :', lis)

    

# append_user_input(lis)




''' Exercise - Raising exceptions
Write a program to take the square root of user input.
Use a try-except statement to ensure the user inputs a float.
If the user inputs a negative number, raise a ValueError that will also be caught by the except statement. Make sure to write a descriptive message in the exception you raise.
'''
import math


# while True:
#    try:
#       userin = float(input("Input your number: "))
#       if userin < 0:
#         raise ValueError
#    except ValueError:
#       print("Input must enter a float and it cannot be negative")
#    else:
#       print(math.sqrt(userin)) 
#       break

def avg_2_nums(x, y):
      return (x + y) / 2

num1 = 5
num2 = 4

try:
      print(avg_2_nums(num1, num2))
except TypeError:
    print("We can catch the error for our function call")
finally:
     print("Lets do something else over and over again")
      
# print(avg_2_nums(num1, num2))



# Propogating exceptions (functions)

# def average_two_numbs(x,y):
#     return (x + y) / 2

# num1 = 5
# num2 = 'hello'

# print(average_two_numbs(num1,num2))

# try:
#     print(average_two_numbs(num1, num2))
# except TypeError:
#     print('we can catch the error for our function call')
# finally:
#     print('')

# price = 0

# def calculate_final_price(price, tax):
#     return price * tax
#     print(calculate_final_price)

# total = calculate_final_price(float(input('what is the price: ')), .5)
# print(total)
