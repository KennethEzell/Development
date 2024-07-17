
''' Print statement outlining rules for your application'''
print()
print(f"**User Name Requirements**")
print("- Must start with a lowercase letter and only contain letters, numbers, and underscores.")
print("- Cannot be in the list of the following usernames: admin, admin123, user1, superuser")
print()
print("**Password Requirements**")
print("- Contains at least 8 characters")
print("- Contains at least on uppercase letter")
print("- Contains at least opne lowercase letter")
print("- Contains at least one digit")
print("- Contains at least one of the following: !, ?, @, #, $, ^, &, *, _, - ")
print("- Doesnot contain any spaces")
print()


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
username = ""
userpassword =""
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
              "Incorrect Username, please try again.  ",
              "Incorrect Password, please try again.  ",
              "Incorrect Username or Password"]

''' Start your while loop '''

while True:
    has_digit = 0
    contains_must_haves = 0 
    no_spaces  = 0
    has_errors = 0 # stored value to verify no errors before asking for final login #
    
#Get your username and password#

    print()
    username = input('Please enter your username: ') 
    userpassword = input('Please enter your password: ')
    print()

# stop - break command to end loop #

    if username == 'stop':
        print("Sign up canceled")
        break
    if userpassword == 'stop':
        print("Sign up canceled")
        break
# Test your username and enforce logic #

    if username[0].isupper():
        print(error_msgs[0])
        # print(username[0])
    # if username.istitle(): # check if first letter of username is upercase
        # print(error_msgs[0])
        # print()

    if username in taken_user_names: # check if username is in the reserved list. Return error if so
        print(error_msgs[1])
        has_errors += 1
        # print()
        
    if not username.isidentifier(): # check if username contains alphanumeric or '_'. Return error if not
        print(error_msgs[2])
        has_errors += 1
        # print()

    # Test user password logic #

    if len(userpassword) < 8: # password must contain at least 8 characters
        print(error_msgs[3])
        has_errors += 1
        # print()

    if userpassword.lower() == userpassword: # password must contain at least one uppercase character
        print(error_msgs[4])
        has_errors += 1
        # print()

    if userpassword.upper() == userpassword: # password must contain at least one lowercase character
        print(error_msgs[5])
        has_errors += 1   

    for i in userpassword:
        if i.isdigit():
            has_digit += 1
        elif i in must_haves_in_password:
            contains_must_haves += 1
        elif i == ' ':
            no_spaces += 1
      
    if has_digit < 1: # check password for at least 1 digit
        print(error_msgs[6])
        has_errors += 1
        # print()
        
    if contains_must_haves < 1: # check password for one of the must have characters
        print(error_msgs[7])
        has_errors += 1
        # print()
        
    if no_spaces > 0:
        print(error_msgs[8]) # check password for blank spaces
        has_errors += 1
        
            
    
        

# If we pass, congratulate the user and immediately ask them to register #
    if has_errors == 0:
        print('Sign Up Successful!')
        print('Please sign in')

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



