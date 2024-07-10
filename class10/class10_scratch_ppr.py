# while True:
#     username = input('Please enter your username: ') #''' Get your username and password'''
#     print(username)
#     if username[0].islower():
#         print('Good job, your first letter is lowercase')
#         break
#     elif username[0].islower() is not True:

#         print('Your first letter must be lower case.')
#     continue
     
# for x in range(16, 2, -3):
#     print(x, end=' ')

# for i in range(4):
#     print(i, i+i,sep=', ')
# for x in range(1960, 2001, 5):
#     print(x, end=' ')

# for x in range(30, -1, -1):
#     print(x, end=' ')

# planets = ["mercury", "venus", "earth", "mars"]
# output = ''
# # 0: mercury, 1: venus, 2: earth, 3: mars

# for x in range(len(planets)):
#     output += f' {x}: {planets[x]},'
# print(output)

# print(f'{x}, {end=' '}')
# print(f'{range(len(planets), )}: {(planets)}, end=', '')

# employees = ['Bob', 'Cynthia', 'Abdul']
# job_titles = ['accountant', 'engineer', 'recruiter']

# for i in range(len(employees)):
#     print(employees[i] + "'s job title is " + job_titles[i])
# output = []

# while True:
#     choice = input('Choose 1, 2, or 3 parameters for your range.')
#     if choice == '1':
#         start1 = int(input('how long is your range? '))
#         output1 = range(start1)
#         for o in output1:
#             print(o, end='')
#             break

#     if choice == '2':
#         start2 = int(input('how long is your range? '))
#         stop2 = int(input('enter your stop value. '))
#         output2 = range(start2,stop2)
#         for o in output2:
#             print(o)
#         break
#     if choice == '3':
#         start3 = int(input('how long is your range? '))
#         stop3 = int(input('enter your stop value. '))
#         interval3 = int(input('enter your interval. '))
#         output3 = range(start3, stop3, interval3)
#         for o in output3:
#             print(o, end=' ')
#         break
    # if choice == '2':
    #     start2 = int(input('how long is your range? '))
    #     stop2 = int(input('enter your stop value. '))
    #     output2 = range(start2, stop2)
    #     for o in output2:
    #         print(o)
    #     break
    # if choice == '3':
    #     start3 = int(input('how long is your range? '))
    #     stop3 = int(input('enter your stop value. '))
    #     interval3 = int(input('enter your interval. '))
    #     output3 = range(start3, stop3, interval3)
    #     for o in output3:
    #         print(o, end=' ')
    #     break
    # else:
    #     print('you must enter 1, 2, or 3.')
    #     continue


    #     your_range = range(choice)
    #     print(1)
    #     break
    # if choice == '2':
    #     print('you chose 2')
    #     break
    # if choice == '3':
    #     print('you chose 3')
        # break    #     break
    # elif choice == '2':
    #     print('you chose 2. ')
    # elif choice == '3':
    #          print('you chose 3. ')
    # break


 
while True:

    choice = input("Choose 1, 2, or 3 parameters for your range. ")


    if choice == '1':
        start_1 = int(input("How long is your range: "))
        output_1 = range(start_1)
        for o in output_1:
            print(o, end=' ')
        break

    