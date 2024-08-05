
# Functions Part 2

# With doc string and type hinting

# def my_function(country: str = "Norway") -> None:
#     print("I am from " + country)
#     return country

# my_function()
# my_function('sweeden')
# my_function('brazil')
# my_function('india')


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

# def center(list_nums, use_median=False):
#     if use_median:
#         result = statistics.median(list_nums)
#     else:
#         result = statistics.mean(list_nums)
#     return result

def center(list_nums, use_median=False):
    if use_median:
        return statistics.median(list_nums)
    else:
        return statistics.mean(list_nums)
    

# print(center(test_list1,True))
# print(center(test_list1))

test_list1 = [1,2,2,2,3,4,5,6,7,8]
test_list2 = [3,6,7,9,10,11,2]

# print(center(test_list2,True))
# print(center(test_list2))

def center(list_nums, use_median=False):
    if use_median:
        return statistics.median(list_nums)
    else:
        return statistics.mean(list_nums)