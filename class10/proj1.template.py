
''' Print statement outlining rules for your application'''



''' Initialize your variables 



'''
'''
We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''
# username

''' A List to handle error messages '''
error_msgs = []


''' Start your while loop '''
while True:
    username = input('Please enter your username: ') #''' Get your username and password'''
    print(username)
    if username[0].islower():
        print('first letter is lowercase')
     
    else: 
        print('First letter must be lower case.')
        username = input('Please enter your username: ')
         
    userpassword = input('Please enter your password: ')
    print(userpassword)
    break


''' Test your username and enforce logic'''


''' Test your password and enforce logic'''



''' If we pass, congratulate the user and immediately ask them to register'''




''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''



