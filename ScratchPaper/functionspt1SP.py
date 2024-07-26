''' Focus on the structure of your functions, let's have fun and learn how they work! :) '''


'''
1. Write as function that converts celsius to fahrenheit
''' 
# snake case for function names

# farenheit = (celsius * 9/5) + 32
 

# def find_farenheit(temperature_in_celcius):
#     farenheit = (temperature_in_celcius * 9/5) + 32
#     print(f'You entered {temperature_in_celcius}')
#     print(farenheit)


# celsius = float(input('Enter the temperature in celsius: ')) # declaring our variable


# find_farenheit(celsius) # this is a function call, nothing will happen unless we have this line of code
     


''' 2. write a function that generates a filename of lastname, firstname, and todays date'''

# from datetime import date

# firstname = 'bill'
# lastname = 'smith'

# def filename_gen(fname, lname):
#     return f'{lname}_{fname}_{date.today()}.txt'


# print(filename_gen(firstname, lastname))

    

'''  3. Function to add two different numbers '''

# num1 = 5
# num2 = 17

# def add_two(value1, value2):
#     numsum = num1 + num2
#     return f'{num1} + {num2} = {numsum}'

# # print(add_two(num1, num2))

# '''   4. Function to reverse a word for example 'team' becomes 'maet' '''
# word = 'kenneth'

# def flip_it(wordx):
#     return word [::-1]

# print(flip_it(word))
    



'''  5. Function that will deliver the average of 2 values '''

# val1 = 15
# val2 = 20

# def get_avg(num1, num2):
#     avg = (num1+num2)/2
#     return avg

# print(get_avg(val1, val2))
    



''' 
 6. Write a function that will loop through a string and print whether a character is or is not a vowel.
'''



'''  7. Write a function that takes a list of these dictionary items. Return the first names from the list of dictionaries in a single list

students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 21}]'''

students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22},
            {'name': 'Charlie', 'age': 21}]





''' Let's print from our functions'''

''' 8.  Create a function that asks the user for their name and greets them back with a hello'''




''' If we print we return none'''



''' 9.  Write a condition that takes a list of students grades, return a dictionary with the students names and grade averages

students = [{'name': 'Alice', 'science':75, 'math':80, 'world history': 90},\
            {'name': 'Bob', 'science':50, 'math':65, 'world history': 88},\
            {'name': 'Charlie', 'science':100, 'math':75, 'world history': 70}]

'''

students = [{'name': 'Alice', 'science': 75, 'math': 80, 'world history': 90},
            {'name': 'Bob', 'science': 50, 'math': 65, 'world history': 88},
            {'name': 'Charlie', 'science': 100, 'math': 75, 'world history': 70}]




'''

10.
Suppose you work for a bank, and you have a list of transactions with the following information for each one: customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}
'''

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},
                {'id': 'b', 'amount': 1350, 'type': 'deposit'},
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'},
                {'id': 'a', 'amount': 1000, 'type': 'deposit'},
                {'id': 'a', 'amount': 75, 'type': 'deposit'},
                {'id': 'a', 'amount': 60, 'type': 'deposit'},
                {'id': 'b', 'amount': 13, 'type': 'withdrawal'}]


list_of_nums = [2, 4, 6, 8, 10, 20]

def avg_of_list(numbers):
    return sum(numbers) / len(numbers)



print(avg_of_list(list_of_nums))
