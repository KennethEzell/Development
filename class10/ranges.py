'''
Ranges
    - Must be integers, whole numbers
    - Used to iterate
    - Does not store all the numbers, but knows what they should be
    - Simple to write and create
    -saves memory
'''

# Using the range function, lets count to 20

# for x in range(21):
#     print(x, end=' ')

# twenty_count = range(21)

# for t in twenty_count:
#     print(t, end=' ')

''' Let's try these '''

# for i in range(16, 2, -3):
#     print(i, end=' ')

# for i in range(4):
#     print(i, i+1, sep=', ')


'''
Write a range that is every five years from 1960 to 2000.
'''
# five_years = range(1960, 2001, 5)

# for e in five_years:
#     print(e , end=' ')

'''
range(start, stop, step)
'''



'''
Write a range that counts down from 30 to 0
# '''
# count_down = range(30, -1, -1)

# for t in count_down:
#     print(t, end=' ')

# my_range = reversed(range(0, 31))
# for i in my_range:
#     print(i, end=' ')
# print(my_range)


'''
Exercise
Rewrite the for loop we made last class that goes through a list and prints each item in the list, along with its index. (Hint: you can use a range, and you won't need a separate counter variable.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars
'''

# planets = ["mercury", "venus", "earth", "mars"]
# output = ''
# # 0: mercury, 1: venus, 2: earth, 3: mars

# for x in range(len(planets)):
#     output += f' {x}: {planets[x]},'
# print(output)

        # print(f'{x}, {end=' '}')
# print(f'{range(len(planets), )}: {(planets)}, end=', '')


''' Exercise
You have a list of employees, and a list of job titles. Assume the lists are the same length and in the same order.
Use one for loop to go through both lists and print the job title of each employee.
For example, if these are your lists:
employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']
This should be your output:
Bob's job title is accountant.
Cynthia's job title is engineer.
Abdul's job title is recruiter.

# '''


# employees = ['Bob', 'Cynthia', 'Abdul']
# job_titles = ['accountant', 'engineer', 'recruiter']

# for i in range(len(employees)):
#     print(employees[i] + "'s job title is " + job_titles[i])

# for x in range(len(employees):
#    print(f'{employees[x]} is an {job_titles}' )

'''
Write some code that creates a range based on what the user enters. 
Challenge: you can make a range with 1, 2, or 3 numbers. How would you allow the user to pick any of these options?
'''

# options = range(3)
# print(options, end='')


while True:

    choice = input('choose 1 2 or 3 parameters for you range. ')

    # if choice == '1':
    #     start_1 = int(input('how long is your range: '))
    #     output_1 = range(start_1)
    #     # for o in output_1:
    #     #  break
    # # if choice == '2':
    # #     start_2 = int(input('How long is start value: '))
    # #     stop_2 = int(input('what is your stop value'))
    # #     output_2 = range(start_2, stop_2)
    # #     for o in output_2:
    # #         print(o, end=' ')
    # #     break

    if choice == '1':
        start_1 = int(input("What is your start value: "))
        output_1 = range(start_1)
        for o in output_1:
            print(o, end=' ')
        break
 
    if choice == '2':
        start_2 = int(input("What is your start value: "))
        stop_2 = int(input("what is your stop value: "))
        output_2 = range(start_2, stop_2)
        for o in output_2:
            print(o, end=' ')
        break


    if choice == '3':
        start_3 = int(input("What is your start value: "))
        stop_3 = int(input("what is your stop value: "))
        interval_3 = int(input("What is your interval value: "))
        output_3 = range(start_3, stop_3, interval_3)
        for o in output_3:
            print(o, end=' ')
        break    
    # if choice == '2':
    #     start_2 = int(input("How long is start value: "))
    #     stop_2 = int(input('What is your stop value: '))
    #     output_2 = range(start_2, stop_2)
    #     for o in output_2:
    #         print(o, end=' ')
    #     break
    #     break

    # if choice == '3':
    #     start_3 = int(input("How long is start value: "))
    #     stop_3 = int(input('What is your stop value: '))
    #     increment = int(input('what is your increment: '))
    #     output_3 = range(start_3, stop_3, increment)
    #     for o in output_3:
    #         print(o, end=' ')
    #     break
    # else:
    #     print('you must enter 1, 2, or 3')
    #     continue