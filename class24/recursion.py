''' Recursion and more brain teasers


FUNCTION
    BASE CONDTION
    RECURSIVE CALL

 '''


''' Lets break Python'''

def i_am_recursion():
    i_am_recursion()


# i_am_recursion()


''' Blast off Recursion Function  

Lets write a recursive function that will count down from nth positve number, down to zero and give a nice message to the user!

'''

# def count_down(n):
#     if n > 0:
#         print(n)
#         count_down(n-1)
#     else:
#         print('Blast off') 
    
# count_down(10)



''' Blast off recursion in a loop '''

# def count_down(n):
#     for i in range(n, 0, -1):
#         print(i)
#     print('Blast off')

# count_down(10)




''' Write a function that will take in a string and will return a list along with the count of each character

Example:

'Saturday'

[S,1,a,2,t,3,u,4,r,5,d,6,a,7,y,8]

'''
# new_list = []
# count = 0
# data = 'Saturday'

# def char_count(word):
#     output = []
#     count = 0
#     for x in word:
#         output.append(x)
#         output.append(count)
#         count += 1
#     print(output)

# char_count(data)


''' Using Recursion, lets write a function that will count down from an even number down to 0

0 is our base case (when our recursion will stop)

Bonus: Lets put a fix in place to let the user know they have to enter an even number
'''

# def count_down_even(n):
#     if n % 2 == 0:
#         if n > 0:
#             print(n)
#             count_down_even(n-2)
#         else:
#             print('Blast off')
#     else:
#         print('Your number must be an even number.')


# count_down_even(20)





''' Write a python function that will take in the following dictionary

acct = {"Name": "Joe Smith", "Session Count": 3, "Cost Per Session": 5.50}

and will output a string

'Hello Joe Smith, your balance is 16.50'

'''

# acct = {"Name": "Joe Smith", "Session Count": 3, "Cost Per Session": 5.50}

# def act_balance(x): print(f'Hello {x['Name'], your balance is {x['Session Count']} * {x[{"Cost Per Session"}
# act_balance(acct{})




''' Factorial
Write a recursive function that will calculate the factorial of a number. The function should take in a number.

How does Factorial work?
n! = n x (n - 1) x (n - 2) x (n - 3) x ... x 1

Factorial of 10
10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1

 '''

# def factorial(n):
#     if n == 1:
#         return n * 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))
# print(5*4*3*2*1)

# def fact_countdown(num):
#     y = 0
#     for x in num:
#         if x > 0:
#             x = x * (x - 1) 
#             print(x)
#             fact_countdown(num-1)
#         else:
#             print(f'Total is ', x)


# fact_countdown(10)


''' Sum of natural numbers
Write a function that calculates the sum of the first n natural numbers down to 1. Use recursion to solve this problem

10 = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1

total of 55
'''
# def nat_sum(x):
#     if x == 1:
#         return x * 1
#     else:
#         return x + nat_sum(x - 1)

# print(nat_sum(10))



# def factorial(n):
#     if n == 1:
#         return n * 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))
# print(5*4*3*2*1)


'''

Exercise
Write a recursive function that multiplies two numbers, using addition.
The function multiply(m, n) should return m*n
'''

def multiply(m, n):
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)
    
# print(multiply(12,4))

#Pats solution
# def mult(m, n):
#   if n <= 0:
#     print(f"Last step. Added a 0 because we're breaking out of the recursion loop.")
#     return 0
#   else:
#     print(f"{n} steps left. Adding another {m}")
#     return m + mult(m, n-1)

# print(mult(5,2))
'''
Using the previous example as reference, write a recursive function that takes one number to the power of another number, using multiplication.
The function power(m, n) should return m**n
'''
# def power(m, n):
#     if n == 1:
#         return m
#     else:
#         return m * power(m, n - 1)
    
# print(power(3, 3))
# def exp(m, n):
#     if n <= 0:
#         return 1
#     else:
#         result = m * exp(m, n-1)
#         print(f"{m} ^ {n} = {m} * {m} ^ {n-1} = {result}")
#         return result

# print(exp(5, 2))

''' More brainteasers, courtesy of https://www.w3resource.com/'''



''' Write a function that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''

# def file_type(name):
#     for x in len(name):
#         if x == '.':

#     # print(len(name))

# file_type('ken')

# Forrest's answer
# file_name = "workbook.notepad"
# def ext_finder(string: str):
#     return string.split(".")[1]

 
# print(ext_finder(file_name))
 



'''
September Challenge 

The Fibonacci sequence is a pattern that often appears in nature. This is the pattern: 1, 1, 2, 3, 5, 8, 13, ...
Each number is the sum of the two numbers before it. So, element n of the Fibonacci sequence can be computed like this: n = (n-1) + (n-2)
Patterns like this lend themselves to recursion very naturally.
How would you write a recursive function that computes the first n digits of the Fibonacci sequence?

'''

