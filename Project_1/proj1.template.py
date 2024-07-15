
''' Print statement outlining rules for your application'''



''' Initialize your variables 



'''
'''
We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''
# username

''' A List to handle error messages '''
error_msgs = ["Username must begin with a lowercase. Please try again. ", 
              "That username is already taken. Please try again.", 
              "Username must be alphanumeric.", 
              "Invalid Password. Must be at least 8 characters long. ",
              "Invalid Password. Must contain at least one uppercase letter. ",
              "Invalid Password. Must contain at least one lowercase letter. ",
              "Invalid Password. Must contain at least on digit. ",
              "Invalid Password. Must contain at least one of the following: !, ?, @, #, $, ^, &, *, _, - ",
              "Invalid Password. Cannot contain any " " (blank) spaces. ",
              "Incorrect Username, please try again.  ",
              "Incorrect Password, please try again.  "
              ]
taken_user_names = ['admin', 'admin123','user1','superuser']

must_haves_in_password = ['!', '?', '@', '#', '$', '^', '&', '*', '_', '-' ]

''' Start your while loop '''
while True:

#''' Get your username and password'''

    username = input('Please enter your username: ') 
    

#''' Test your username and enforce logic'''

    if not username.islower(): # check first character is lower case, return error message if not
        print(error_msgs[0])     
        continue
    elif username in taken_user_names: # check if username is in the reserved list. Return error if so
        print(error_msgs[1])
        continue
    elif not username.isidentifier(): # check if username contains alphanumeric or '_'. Return error if not
        print(error_msgs[2])
        continue
    break

while True:

# Get userpassword
    userpassword = input('Please enter your password: ')
    has_digit = 0
    contains_must_haves = 0 
    no_spaces  = 0

    if len(userpassword) < 8: # password must contain at least 8 characters
        print(error_msgs[3])
        continue
    if userpassword.lower() == userpassword: # password must contain at least one capital character
        print(error_msgs[4])
        continue
    if userpassword.upper() == userpassword: # password must contain at least one lowercase character
        print(error_msgs[5])
        continue
        
    for i in userpassword:
        if i.isdigit():
            has_digit += 1
        elif i in must_haves_in_password:
            contains_must_haves += 1
        elif i == ' ':
            no_spaces += 1
            continue
    if has_digit < 1:
        print(error_msgs[6])
        continue
    if contains_must_haves < 1:
        print(error_msgs[7])
        continue
    if no_spaces > 0:
        print(error_msgs[8])
        continue
    if no_spaces < 1:
        print(f'Good, no blank spaces in password. ')
    if has_digit > 0:
        print(f'Password has {has_digit} numbers. ')        
    if contains_must_haves > 0:
        print(f'Password has {contains_must_haves} must have characters. ')
        print('Good job')    
        break
    
    break


    break
print(f'Your username is: {username} ')
print(f'Your password is: {userpassword} ')
print()
print()
print('Sign up successful!')
print()
print()
print('Please enter username and password. ')

while True:  

    test_username = input("Username: ")
    if test_username != username:
        print()
        print(error_msgs[9])
        print()
        continue
    if test_username == username:
        print()
        print('Username Verified!')
        print()
        
      
    test_userpassword = input("User Password: ")
    if test_userpassword != userpassword:
        print()
        print(error_msgs[10])
        print()
        continue
    if test_userpassword == userpassword:
        print()
        print('Login Successful!!')
        print()
        break   








''' If we pass, congratulate the user and immediately ask them to register'''




''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''



