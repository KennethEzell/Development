

# Write a while true loop that will keep asking the day of the week until you type in Monday

# while True:
#     # query user input
    
#     userin = input('Please enter the day of the week: ').casefold()  
    
#     # conduct testing
    
#     if userin == 'monday':
#         print('That is the correct answer. ')
#         break

# animals = ['cat', 'dog', 'bird', 'giraffe'] 

# append() Adds an element at the end of the list

# days = ['sunday', 'monday']

# days.append('tuesday')

# print(days)

# clear() Removes all the elements from the list

# months = ['january', 'february']

# months.clear()

# print(months)

# copy() Returns a copy of the list

copy_me = [1, 2, 6]

newcopy = copy_me.copy()

# print(newcopy)
# print(type(newcopy))

# count() Returns the number of elements with the specified value
# three_cheers = ['hooray', 'hello', 'hooray']

# print(three_cheers.count('hooray'))

# new_users = ['Sally', 'Mohammad']
# current_users = ['Ted', 'Brad', 'Charlie']

# current_users.extend(new_users)

# print(current_users)

# index() Returns the index of the first element with the specified value

# cartoons = ['bugs bunny', 'minnie mouse', 'daffy duck']

# minnies_index = cartoons.index('bugs bunny')

# print(minnies_index)

# planets = ["mercury", "venus", "earth", "mars"]
# count = 0
# output = ''

# for x in planets:
#     numplanet = f'{x.index(x)}:{x} '
#     output += numplanet 
#     count += 1 

# print(output)

old_list = ['Wednesday','Thursday', 'Friday', True, ['blue', 'green', 'red'], {"First Name": "Michelle"}, 12.23, {'Sunday', 'Monday', 'Tuesday'}, (1, 2, 3, 4, 5)]

# new_list = []

# for x in old_list:
#     # print(type(x), x)

#     new_list.append(type(x))
# print(new_list)

# no_repeats = list(set(list(new_list)))

# print(no_repeats)

'''
Exercise: List of Pets

You want to make a list containing the names of pets. Keep prompting the user for a pet name until they enter "stop". If it's a new pet, add it to the list. If the list already has that pet, don't add it.

'''
pet = []
pets_name = ''

while True:
    pets_name = input('Please enter the name of your pet: ')
    print(pets_name)
    break