

''' I scoured the interwebs and found some fun problems for us to solve! Lets work through these and have fun learning along the way '''


'''
You have 2 lists, extract and remove the data from one list and place the items in the other. Print your result
'''

# first_list = [1,2,3,4,5,6,7,8,9,10]

# second_list = []


# while first_list:
#     source = first_list.pop(0)
#     second_list.append(source)

# print(first_list)
# print(second_list)


'''
Write a  Python program to check whether the given strings are palindromes or not. Return True otherwise False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes', 'pop', 'racecar', 'bob', 'lol']
Output:
[False, True, True, False, False]

'''

# palindrome_test_list = ['palindrome', 'madamimadam', '', 'foo', 'eyes', 'pop', 'racecar', 'bob', 'lol']
# result_list = []

# def palindrome(list):

#     for word in palindrome_test_list:
#         if word == word[::-1]:
#             result = True
#         else:
#             result = False
        
#         # print(result) test results
#         result_list.append(result)
#     print(palindrome_test_list)
#     print(result_list)


# palindrome(palindrome_test_list)

'''

Write a Python program to find the length of a given list of non-empty strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]
'''

# my_list = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# output = []

# for word in my_list:
#     output.append(len(word))
# print(output)

'''
 Write a  Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
Input: 123456789
Output:
945
Input: 2468
Output:
0
Input: 13579
Output:
945

'''
# establish the 3 test strings for the code #

# test_string = '123456789'
# test_string2 = '2468'
# test_string3 = '13579'

# # build a function to take in the test string, test for odd, mulitple num if odd, or return "0"

# def multiply_odds(data):
#     total = 1 # intialize variable to capture total if num is odd, 
#     is_odd = False # boolean to check if odd numbers are present in string
#     for x in data:
#         num = int(x) # set each number to integer for testing
#         if num % 2 == 1: 
#             total *= num
#             is_odd = True    
#     if is_odd == False: # return "0" if no odd numbers in string
#         print('0 - no odd numbers')
#     else:
#         print(total) # print result if odd numbers are present
   
# multiply_odds(test_string)
# multiply_odds(test_string2)
# multiply_odds(test_string3)

'''
Write a  Python program to find the largest k numbers from a given list of numbers.
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]

Try it with a for loop!
Is there a function in Python that will do this for us??

'''

# test_list = [1, 2, 3, 4, 5, 5, 3, 6, 2]

# y = 0 # intialize variable to capture largest number through test

# for x in test_list: 
#     if x > y: y = x
# print(y)

# # Python function called max used to find the largest num in a list

# largest_k_num = max(test_list)
# print(largest_k_num)


'''
Please turn this:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

into this:
{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
'''

# To be honest, this one took multiple google searches. I'm going over the dictionary class again this weekend #

# convert_me = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# temp_list = ()
# into_dictionary = {}

# convert_me_dic = {char: index for index, char in enumerate(convert_me)}

# print(convert_me_dic)




