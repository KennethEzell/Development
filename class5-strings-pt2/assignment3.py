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
email = email.strip()



# Test 1: It has a "." at the third-to-last index
test_1 = (email[-4] == '.')


# print(f'Test 1: Does {email} has a "." at the tord tp the ;ast index?',test_1)

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
test_2 = ('@' in email[-5::-1])
# print(f'Test 2: {email} has exactlyh one "2" symbol, at the fifth to las index or earlier?', test_2)


# Test 3: There is at least one character before the "@" symbol
test_3 = (email[0] != '@')
print(f'test 3: there is at least one character before the "@" symbol in {email}', test_3)

# Test 4: It doesn’t have any spaces (doesn’t contain " ")
test_4 =(' ' not in email)
print(f'test 4{email} doesnot have sny spaces)', test_4)


# Final Test with AND Keyword
# My work

# Attach
# Upload from this device
# No file chosen
# New
# Points
# No p