''' More fun while true!

Write a while true loop that will keep asking the day of the week until you type in Monday

'''
# while True:
    
#     userinput = input('What day is today?').casefold()
    
    
#     if userinput == 'monday':
#         print('Happy Monday!')
#         break



''' Lists 

Lists store a group of objects (things).
In a list, we can have any type of object.
Unlike strings, lists are mutable.
This means we can change an individual object in a list using index.
We can also add and remove objects from a list.
We can also use lists in a for loop.
'''

''' In a list, we can have any type of object. '''

# i_can_hold_anything = [1, 'cosmos', True, ['blue', 'green', 'red'], {'south', 'east', 5}, {"firstname":'Sonia'}]

# print(i_can_hold_anything)


''' Unlike strings, lists are mutable. This means we can change an individual object in a list using index.'''

# cars = ['honda', 'ford', 'toyota', 'mersedes'] # mersedes is spelled wrong
# cars[3] = 'mercedes'
# print(cars)



''' Lets do some more with indexing '''

# animals = ['cat', 'dog', 'bird', 'giraffe']

# cat = animals[0]
# print(cat)

# dog = animals[1]
# print(dog)

# bird = animals[2]
# print(bird)

# giraffe = animals[3]
# print(giraffe)

'''
Fun with List methods
append() Adds an element at the end of the list
clear() Removes all the elements from the list
copy() Returns a copy of the list
count() Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list
'''

# # append() Adds an element at the end of the list

# days = ['sunday', 'monday']
# days.append('tuesday')
# # print(days)


# # clear() Removes all the elements from the list
# months = ['january', 'february']
# months.clear()
# # print(months)

# # copy() Returns a copy of the list
# copy_me = [1, 2, 6]
# new_copy = copy_me.copy()
# # print(new_copy)

# # count() Returns the number of elements with the specified value
# three_cheers = ['hooray', 'hello', 'hooray']
# # print(three_cheers.count('hello'))


# # extend() Add the elements of a list (or any iterable), to the end of the current list

# new_users = ['Sally', 'Mohammad']
# current_users = ['Ted', 'Brad', 'Charlie']

# current_users.extend(new_users)

# # print(current_users)


# # index() Returns the index of the first element with the specified value

# cartoons = ['bugs bunny', 'minnie mouse', 'daffy duck']
# minnies_index = cartoons.index('minnie mouse')
# # print(minnies_index)


# insert() Adds an element at the specified position

coding_language = 'Python'
other_languages = ['Javascript', 'Java', 'R']
other_languages.insert(0, coding_language)
# print(other_languages)


# pop() Removes the element at the specified position

weather = ['sunny', 'rainy', 'mild']
# print(weather)
# weather.pop(1)
# print(weather)


# remove() Removes the first item with the specified value

movies = ['avengers endgame', 'avengers endgame', 'dune', 'frozen']
movies.remove('avengers endgame')
# print(movies)

# # reverse() Reverses the order of the list
num_list = [1, 2, 3, 4, 5, 6]
num_list.reverse()
# print(num_list)

# sorted() sorts the list
letters = ['z', 'b',  'f', 'r']
letters.sort()
# print(letters)


# sort() Sorts the list

# letters = ['z', 'b',  'f', 'r']
# letters.sort()
# # print(letters)
# new_letters = sorted(nums)

# print(new_letters)


nums = [4, 5, 10, 19.8, 1, 1004]
nums.sort()

# print(nums)

new_nums = sorted(nums)
new_letters = sorted(letters)
# print(new_nums, new_letters)



''' Exercise

Create a for loop that goes through a list and prints each item in the list, along with its index. (Hint: Create a separate counter variable to keep track of the index.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars

'''

# planets = ["mercury", "venus", "earth", "mars"]
# count = 0
# output = ''
# while True:
#     for x in planets:
#         num_planets = f'{count}: {x}'
#         output += num_planets
#         count += 1
        
#         print(f'{x}: [planets])
#         continue

''' Exercise

Write some code that takes one list and creates a second list that has the type for each entry in the list. Hint: Use the type() function and a for loop

Optional:
Make sure you filter out any repeats.

'''

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
# pet = []
# petsname = ''

# while True:
#     petsname = input('Please enter the name of your pet!: ')

#     if petsname == 'stop':
#         break

#     elif petsname not in pet:
#         # petsname = petsname.title()
#         pet.append(petsname)
#         print(f'We have just added {petsname} to your pets list')
#     else:
#         print(f'{petsname} is already in your list')

# print(pet)
    

'''
Example: Removing Values
You have a list of numbers, but it contains multiple of the number 2. Remove the number 2 until it only appears in the list once.

'''

removing_values = [1, 2, 3, 2, 2, 3, 4, 5, 6, 2, 2, 2, 2, 2, 1, 1, 5, 6, 5]

count = 0
# newlist = ''
# while True:
#     for x in removing_values:
#         if x == 2:
#             count += 1
#             x += newlist
#         elif x == 2:
#             x.clear()
#         else:
#             x += newlist
#     break
#####################################

# countoftwo = removing_values.count(2)
# print(countoftwo)

# while removing_values.count(2) != 1:
#     removing_values.remove(2)

# print(removing_values)
'''

Exercise: Removing All Duplicates
You have a list storing important data for your company, but it contains some duplicate entries. Go through your list and remove all the duplicates. When you're done, each item should appear in the list exactly once.
Hint: How would you expand our previous example, which removed duplicates of one value, to remove duplicates of all values?
Hint 2: You might want to make a copy of the original list to use as reference. You may want to use more than one loop.

'''


# original list
states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']
# create a copy
copystates = states.copy()

# capture duplicates
uniquestates = list ()

for s in copystates:
    if s not in uniquestates:
       uniquestates.append(s)

print(uniquestates)
    
    
# copystates = set(copystates)


print(copystates)
