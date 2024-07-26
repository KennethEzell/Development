'''
I decided to place the print command inside of the definition and performed a function call to assign the list of numbers to the parameter "numbers" '''

list_of_nums = [2, 4, 6, 8, 10, 20, 30] # list of numbers for the function


def avg_of_list(numbers): # set definition title and parameter

    # below I perform the calculation within the print command and returned the result 
    return print(f"The average of the {len(numbers)} numbers in the list is {sum(numbers) / len(numbers)}") 

avg_of_list(list_of_nums) # function call



''' Below was my first run at the problem, but I felt the code above was cleaner. Both versions had the same results upon testing.  I apologize if I have unnecessarily complicated the problem.   

def avg_of_list(numbers): # set definition title and parameter
    return sum(numbers) / len(numbers) # return the calculation for the avg of the list of numbers
    
print(avg_of_list(list_of_nums)) # print the result of the function call

'''