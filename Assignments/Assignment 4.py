
def calculate_final_price(): # Establish Function Name

# While loop to get user input and test #

    while True: 

# Get price and tax variables, test both inputs with float, return error if not numbers and loop back for inputs #
        
        try: 
            price = float(input("Please enter the product price: "))
        except ValueError:
            print('Price must be a number')
            continue
        try:
            tax = float(input("Please enter the tax rate: "))
        except ValueError:
            print('Tax must be a number between 0 and 1')
            continue

# Test if inputs pass requirements: price greater than 0 and tax between 0 and 1, return error msgs if fail and repeat inputs #
        try:    
            if price < 0 or tax > 1 or tax < 0:
               raise ValueError
        except ValueError:
            print("The price must be a positive number and the tax must be between 0 and 1")  
        
 # Final price is calculated and printed. While loop is terminated if no errors #        
        else:    
            print(f'Your final price is: $', "{:.2f}".format(price + (price * tax)))
            print('Thank You.  Have a Great Day!') # Added Thank you msg because it just felt right :) #    
            break   
        
# Call the Function #

calculate_final_price()