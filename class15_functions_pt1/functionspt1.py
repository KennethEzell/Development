''' Focus on the structure of your functions, let's have fun and learn how they work! :) '''


'''
1. Write as function that converts celsius to fahrenheit
'''
# snake case for function names

# fahrenheit = (celsius * 9/5) + 32
# def find_fahrenheith(temperature_in_celsius):
#     fahrenheit = (temperature_in_celsius * 9/5) + 32
#     print(fahrenheit)
    
# #     print(f'You selected {temperature_in_celsius}')

# celsius = 20

# find_fahrenheith(celsius) # this is a function call, notheing will happen uness we have a function call

''' cain's code
def convert_c():
    celsius = float(input("Enter the temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in fahrenheit is: {fahrenheit}" )
 
convert_c()'''


''' 2. write a function that generates a filename of lastname, firstname, and todays date'''

# from datetime import date

# firstname = 'bill'
# lastname = 'smith'

# def filename_gen(fname, lname):
#     return f'{lname}_{fname}_{date.today()}.text'
    

# final_file_name = filename_gen(firstname, lastname)

# # print(filename_gen(firstname, lastname))

# '''  3. Function to add two different numbers '''

# def sum_nums(num1, num2):
#     total_nums = num1 + num2
# #     print(f'{num1} + {num2} = {total_nums}')

# two_num_total = sum_nums(10, 20)

# # print (two_num_total)



'''   4. Function to reverse a word for example 'team' becomes 'maet' '''

# txt = "hello world"[::-1]
# print(txt)

# def reverse_string(test_string):
#     flip_it = test_string[::-1]
#     print(flip_it)

# answer = reverse_string(flip_it)


'''  5. Function that will deliver the average of 2 values '''

# val1 = 55
# val2 = 70

# def average(a,b):
#     average = mean([a,b])
#     return average

# print(average(val1, val2))




''' 
 6. Write a function that will loop through a string and print whether a character is or is not a vowel.
'''
# word = 'hooray'

# def vowel_check(word):
    
#     vowels = 'aeiou'

#     for w in word:
#         if w in vowels:
#           print(f'{w} is a vowel')
     
#           else:
#            print(f'{w} is not a vowel')

# vowel_check(word)


'''  7. Write a function that takes a list of these dictionary items. Return the first names from the list of dictionaries in a single list

students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 21}]'''

students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22},
            {'name': 'Charlie', 'age': 21}]

# def first_name(students): # this function accepts a list of dictionaries
#     output = [] # this will hold our first names
#     for s in students:
#         name = s['name']
#         output.append(name)
#     return output

# students_first_names = first_name(students)

# print(students_first_names)
# print(type(students_first_names))      

# first_name(students)


''' Let's print from our functions'''

''' 8.  Create a function that asks the user for their name and greets them back with a hello'''

# def greeting(input('whats your name? ')):
#     output = print(f'Hello {greeting}')
#     return output

# Cains solution
# greeting()
# def greet():
#     name = input("What is your name? ")
#     print(f"Hello {name}")
# greet()


''' If we print we return none'''



''' 9.  Write a condition that takes a list of students grades, return a dictionary with the students names and grade averages

students = [{'name': 'Alice', 'science':75, 'math':80, 'world history': 90},\
            {'name': 'Bob', 'science':50, 'math':65, 'world history': 88},\
            {'name': 'Charlie', 'science':100, 'math':75, 'world history': 70}]

'''

students = [{'name': 'Alice', 'science': 75, 'math': 80, 'world history': 90},
            {'name': 'Bob', 'science': 50, 'math': 65, 'world history': 88},
            {'name': 'Charlie', 'science': 100, 'math': 75, 'world history': 70}]



# def gpa(students):
#     grade_averages = {}

#     for s in students:
#         name = s['name']
#         science = s['science']
#         math = s['math']
#         world_history = s['world history']
#         gpa = (science + math + world_history)
#         grade_averages.update({name:gpa})
#     return grade_averages



     #    print(name, science, math, world_history)


    
# from statistics import mean
# def gpa(student):
#     output = {}
#     for s in student:
#         name = s["name"]
#         grades = [s["science"], s["math"], s["world history"]]
#         gpa = mean(grades)
#         output[name] = gpa
#     return output
# print(gpa(students))
 


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


# def customer_totals(banking):
#     register = {}
#     for t in transactions:
#      if transactions('id') == 'a':
#         if transactions('type') == 'deposit':
#            append.register()

def account_balances(transactions):
   balances = {}
   for t in transactions:
     transaction_type = t['type']
     amount = t['amount']
     transaction_id = t['id']

     if transaction_id not in balances:
          balances.update({transaction_id: amount})
     
# print(account_balances(transactions))
