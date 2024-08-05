
# Functions Part 2

# With doc string and type hinting

# def my_function(country = "Norway"):
#     print("I am from " + country)


# my_function('Sweeden')
# my_function('India')
# my_function()
# my_function('Brazil')

# def test_function(name):
#     print(name)
#     return name

# test_function('hello')

# users_name = test_function('Joe')

# print(users_name)

'''
Exercise
Write a function called center that returns either the mean or median of a list of numbers.
This function should take two parameters: A list of numbers, and an optional parameter called use_median which should default to False.
If use_median is False, return the mean of the list.
If use_median is True, return the median of the list.
Test your function by calling it with different arguments.
'''


import statistics

test_list1 = [1,2,2,2,3,4,5,6,7,8]
test_list2 = [3,6,7,9,10,11,2]

# def center(list_of_numbers, use_median = False):
#     num = sum(test_list1) / len(test_list1)
#     if use_median:
#         # output = statistics.median(list_of_numbers)
#         return statistics.median(list_of_numbers)
#         # return output
#     else:
#         return statistics.mean(list_of_numbers)
#         # return output
        

#     print(num)
# print(center(test_list1, True))
# print(center(test_list1))
# print(center(test_list1))
# # center(test_list1)


# import statistics
# def center(num_list = [], use_median = False):
#     if use_median:
#         return statistics.median(num_list)
#     else:
#         return statistics.mean(num_list)
   
# print(center([1, 2, 7, 4, 5]))


# '''Documentation, type hinting, shorthand if-then-else'''


# Returning multiple values

# def get_vowels_and_consonants(word):

#     vowels = ''
#     consonants = ''
#     for letter in word:
#         if letter in 'aeiou':
#             vowels += letter
#         else:
#             consonants += letter

#     return vowels, consonants    


# vowels, consonants = get_vowels_and_consonants('apple')
# print(vowels)
# print(consonants)


'''
Exercise
Write a Python function called get_stats that takes in a list of numbers and returns the following three values: The mean, the median, and the mode of the list.
Call the function on a list, and print each statistic on a separate line.
my_list = [1,2,4,5,5]
Output:
Mean: 3.4
Median: 4
Mode: 5
'''

my_list = [1,2,4,5,5]
# def get_stats(my_list):
#     my_mean = statistics.mean(my_list)
#     my_median = statistics.median(my_list)
#     my_mode = statistics.mode(my_list)
#     return my_mean, my_median, my_mode

# get_stats
# print(get_stats(my_list)) 
# print(get_stats(my_list))
# print(get_stats(my_list))
'''Global variables'''

x = "challenging"

# def change_x():
#        x = "fun"

# change_x()
# print(x)



'''
A lambda is a small anonymous function. It can take any number of arguments, but it can only have one expression, which is returned.
Syntax: lambda arguments : expression
'''

# Function to add two numbers
def add_two(x, y):
    return x + y 

# print(add_two(5, 10))
    
# Written as a Lambda

lambda x, y: x + y

add_two_lambda = lambda x, y: x + y

# print(add_two_lambda(9, 15))

# print((add_two_lambda)(5,10))

# # Write the following functions as Lambdas

# def greeting(fname):
#     print(f'Hello, {fname}')

# lambda fname: f"Hello {fname}"

# hello_name = lambda fname : f"Hello {fname}"

# print(hello_name('joe'))

#  like 1
 

# first = lambda fname: 'kenneth'
# greeting(first)

# greeting("Sally")


# def double_me(num):
#     return num + num

# print(double_me(500))

# lambda num: num + num
# print(double_me_two(5))

'''
Exercise
Write a function that computes the n-th power of a number, given two arguments, num and n.
Now, write a lambda that is equivalent to that function.
'''
# function
# def exponents(num,n):
#     exp = num**n
#     return exp

# print(exponents(5,3))

# lambda




''' Higher Order Functions
These are functions that may accept a function as an argument or return a function as its output. In Python, reduce(), map() and filter() are some of the most important higher-order functions. When combined with simpler functions, they can be used to execute complex operations.

filter - The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

map - returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

'''
# Let's use filter() to find the even numbers in a list 
# filter(fun, iter)

# def even_nums(n):
#     return n % 2 == 0

# print(even_nums(6))

# Function


# # Lambda
# even_nums = lambda n : n % 2 == 0
# print(even_nums)


my_list = [0,1,2,3,4,5,6,7,8,9,10]




# Let's use map() to multiply every value in this list by 3
# map(fun, iter)

triple_me = [0,1,2,3,4,5,6]
# Function




# Lambda



# Lambda with sort
# sorted(iterable, key=key, reverse=True/False)

students = [{"name":"Kim","grade":98},
            {"name":"Joe","grade":65},
            {"name":"Ted","grade":93},
            {"name":"Keisha","grade":80},
            {"name":"Torrie","grade":65},
            {"name":"Simon","grade":78}]



''' 
Write a lambda function that makes a string a title case and apply the function to the list below with a map function
words = ['make', 'us', 'title', 'case']

'''



''' Write a lambda function that will add ten to a list item if that list item is greater than or equal to 50, otherwise it will subtract five

my_numbers = [50, 12, 19, 80, 5, 75]
'''

''' Write a lambda function and utilize reduce to add all the numbers in this list

add_me_up = [50, 12, 9, 100, 56, 70]
'''