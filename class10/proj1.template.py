
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

#''' Get your username and password'''

    username = input('Please enter your username: ') 
    

#''' Test your username and enforce logic'''

    if username[0].islower():
        print('Great! Your first letter is lowercase')
     
    else: 
        print('Your first letter must be lower case.')
        username = input('Please enter your username: ')

 #''' Test your password and enforce logic'''
         
    userpassword = input('Please enter your password: ')
    print(userpassword)

    break









''' If we pass, congratulate the user and immediately ask them to register'''




''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''



