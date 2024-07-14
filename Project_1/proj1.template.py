
''' Print statement outlining rules for your application'''



''' Initialize your variables 



'''
'''
We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''
# username

''' A List to handle error messages '''
error_msgs = ["Username must begin with a lowercase. Please try again. ", "That username is already taken. Please try again.", "Username must be alphanumeric."]
taken_user_names = ['admin', 'admin123','user1','superuser']

''' Start your while loop '''
while True:

#''' Get your username and password'''

    username = input('Please enter your username: ') 
    

#''' Test your username and enforce logic'''

    if not username.islower():
        print(error_msgs[0])     
        continue
    elif username in taken_user_names:
        print(error_msgs[1])
        continue
    elif not username.isidentifier():
        print(error_msgs[2])
        continue


    userpassword = input('Please enter your password: ')
    print(userpassword)

    break









''' If we pass, congratulate the user and immediately ask them to register'''




''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''



