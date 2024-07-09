while True:
    username = input('Please enter your username: ') #''' Get your username and password'''
    print(username)
    if username[0].islower():
        print('Good job, your first letter is lowercase')
        break
    elif username[0].islower() is not True:

        print('Your first letter must be lower case.')
    continue
     