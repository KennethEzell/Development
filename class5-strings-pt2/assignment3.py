# Back

# Not turned in

# Turn in
# Assignment 3 - Testing Strings
# Due June 21, 2024 8:00 PM
# Instructions
'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 
email = input('Hello, pleasse enter your email. ')


# Clean data
email = email.strip() # clean email input with strip method
# print(email)
# print(len(email))

# Test 1: It has a "." at the third-to-last index
test_1 = (email[-4] == '.')
# print(test_1)


print(f'Test 1: Does {email} has a "." at the third-to-last index?',test_1)

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
test_2 = ('@' in email[-5::-1])
# print(email[-5::-1])
print(f'Test 2: {email} has exactly one "@" symbol, at the fifth to last index or earlier?', test_2)


# Test 3: There is at least one character before the "@" symbol
test_3 = (email[0] != '@')
# test_3b =(email.index('@') > 0) # This an alternative solution to check if at least one character before '@'
print(f'Test 3: there is at least one character before the "@" symbol in {email}', test_3)

# Test 4: It doesn’t have any spaces (doesn’t contain " ")
test_4 =(' ' not in email)
print(f'Test 4: {email} doesn\'t have any spaces (doesn\'t contain" ")', test_4)


# Final Test with AND Keyword
all_tests = test_1 and test_2 and test_3 and test_4
print(f'Is {email} valid?', all_tests)
# My work

# Attach
# Upload from this device
# No file chosen
# New
# Points
# No p