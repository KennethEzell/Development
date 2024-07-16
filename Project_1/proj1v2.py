
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
sys_username = ""
sys_userpassword = ""

''' Tables for unavailable user names, and necessary characters for password '''

taken_user_names = ['admin', 'admin123','user1','superuser']

must_haves_in_password = ['!', '?', '@', '#', '$', '^', '&', '*', '_', '-' ]


''' A List to handle error messages '''

error_msgs = ["Username must begin with a lowercase. ", 
              "That username is already taken.", 
              "Invalid Username. Username must be alphanumeric or _ .", 
              "Invalid Password. Must be at least 8 characters long. ",
              "Invalid Password. Must contain at least one uppercase letter. ",
              "Invalid Password. Must contain at least one lowercase letter. ",
              "Invalid Password. Must contain at least on digit. ",
              "Invalid Password. Must contain at least one of the following: !, ?, @, #, $, ^, &, *, _, - ",
              "Invalid Password. Cannot contain any " " (blank) spaces. ",
              "Incorrect Username, please try again.  ",
              "Incorrect Password, please try again.  "]

''' Start your while loop '''

while True:
    
#Get your username and password#

    print()
    username = input('Please enter your username: ') 
    userpassword = input('Please enter your password: ')
    print()

#Test your username and enforce logic#

    if username.istitle(): # check if first letter of username is upercase
        print(error_msgs[0])
        # print()

    if username in taken_user_names: # check if username is in the reserved list. Return error if so
        print(error_msgs[1])
        # print()
        
    if not username.isidentifier(): # check if username contains alphanumeric or '_'. Return error if not
        print(error_msgs[2])
        # print()

    # Test user password #

    if len(userpassword) < 8: # password must contain at least 8 characters
        print(error_msgs[3])
        # print()

    if userpassword.lower() == userpassword: # password must contain at least one capital character
        print(error_msgs[4])
        # print()
        


    
# 




''' Test your password and enforce logic'''



''' If we pass, congratulate the user and immediately ask them to register'''




''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''



