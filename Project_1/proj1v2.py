
''' Print statement outlining rules for your application'''

print(f'''

**User Name Requirements**"
- Must start with a lowercase letter and only contain letters, numbers, and underscores.
- Cannot be in the list of the following usernames: admin, admin123, user1, superuser

**Password Requirements**
- Contains at least 8 characters
- Contains at least on uppercase letter
- Contains at least opne lowercase letter
- Contains at least one digit
- Contains at least one of the following: !, ?, @, #, $, ^, &, *, _, - 
- Does not contain any spaces
''')
 



#     )
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


''' Initialize your variables 


We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''
username = ''
userpassword =''
login_username = ""
login_userpassword = ""


''' Tables for unavailable user names, and necessary characters for password '''

taken_user_names = ['admin', 'admin123','user1','superuser']

must_haves_in_password = ['!', '?', '@', '#', '$', '^', '&', '*', '_', '-' ]


''' A List to handle error messages '''

error_msgs = ["Invalid Username. Username must begin with a lowercase. ", 
              "That username is already taken.", 
              "Invalid Username. Username must be alphanumeric or _ .", 
              "Invalid Password. Must be at least 8 characters long. ",
              "Invalid Password. Must contain at least one uppercase letter. ",
              "Invalid Password. Must contain at least one lowercase letter. ",
              "Invalid Password. Must contain at least one digit. ",
              "Invalid Password. Must contain at least one of the following: !, ?, @, #, $, ^, &, *, _, - ",
              "Invalid Password. Cannot contain any blank spaces. ",
              "Incorrect Username or Password, please start over.  "]

''' Start your while loop '''

while True:
    has_digit = 0
    contains_must_haves = 0 
    no_spaces  = 0
    has_errors = 0 # stores count value to verify if any errors occur in username or userpassword before proceding to final login #
    
#Get your username and password#

    print()
    username = input('Please enter your username: ') 
    userpassword = input('Please enter your password: ')
    print()
    username = username.strip() # Removes any blank spaces before or after username
    userpassword = userpassword.strip() # Removes any blank spaces before or after userpassword
    
# stop - break command to end loop #

    if username.lower() == 'stop': # converts username 'stop' to all lowercase to check for break command
        print("Sign up canceled")
        break
    if userpassword.lower() == 'stop': # converts userpassword 'stop' to all lowercsae to check for break command
        print("Sign up canceled")
        break

# Test your username and enforce logic #
    
    if username[0].isupper(): # check if first letter of username is uppercase, if yes, report error
        print(error_msgs[0])        

    if username in taken_user_names: # check if username is in the reserved list. Return error if so
        print(error_msgs[1])
        has_errors += 1        
        
    if not username.isidentifier(): # check if username contains alphanumeric or '_'. Return error if not
        print(error_msgs[2])
        has_errors += 1      

    # Test user password for qualifications #

    if len(userpassword) < 8: # password must contain at least 8 characters
        print(error_msgs[3])
        has_errors += 1       

    if userpassword.lower() == userpassword: # password must contain at least one uppercase character
        print(error_msgs[4])
        has_errors += 1
        # print()

    if userpassword.upper() == userpassword: # password must contain at least one lowercase character
        print(error_msgs[5])
        has_errors += 1   

    for i in userpassword: # check password to verify it contains at least one digit, at least one "must have" character, and no spaces
        if i.isdigit(): # if loop to check each character of password for a digit
            has_digit += 1
        elif i in must_haves_in_password: # if loop to check password for "must have" characters
            contains_must_haves += 1
        elif i == ' ': # if loop to check password for blank spaces
            no_spaces += 1
      
    if has_digit < 1: # if password has no digits, report error message and trip error counter
        print(error_msgs[6])
        has_errors += 1       
        
    if contains_must_haves < 1: # check password for one of the must have characters, if not, report error and trip error counter
        print(error_msgs[7])
        has_errors += 1       
        
    if no_spaces > 0:# check password for blank spaces, if so, report error and trip error counter
        print(error_msgs[8]) 
        has_errors += 1        
        

# If we pass, congratulate the user and immediately ask them to register #

    if has_errors == 0: # checks error counter, if no errors, continue with official sign in
        print('Sign Up Successful!')
        print('Please sign in')
        print()


        login_username = input("Please enter your username: ")
        login_password = input("Please enter your password: ")

# If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch.#
    
        if login_username  == username and login_password == userpassword: #
            print()
            print("LOGIN SUCCESSFUL!")
            print()
            break
        elif login_username != username or login_password != userpassword:
            print(error_msgs[9])
    

    














'''  '''



