# while True:
    
#     price = float(input("Please enter the product price: "))
#     tax = float(input("Please enter the tax rate: "))
#     new_price = 0

#     try:
#         if price < 0 or tax > 1 or tax < 0:
#             raise ValueError
#     except ValueError:
#         print("The price must be a positive number and the tax must be between 0 and 1")  
#     else:
#         print("no errors so far")
#         new_price = price + (price * tax)
        
#         break



def calculate_final_price():
    while True:
        price = float(input("Please enter the product price: "))
        tax = float(input("Please enter the tax rate: "))

        try:
            if price < 0 or tax > 1 or tax < 0:
               raise ValueError
        except ValueError:
            print("The price must be a positive number and the tax must be between 0 and 1")  
        else:    
            print(f'Your final price is: $', (price + (price * tax)))     
            break   
        

# calculate_final_price(float(input("Please enter the product price: ")), float(input("Please enter the tax rate: ")))
calculate_final_price()

#     if price < 0:
#         raise ValueError
# except ValueError:

#    
    

# print(calculate_final_price(10.00, .05))




# def calculate_final_price(price, tax):
#     if price < 0:
#         raise ValueError
#     except ValueError:
#     print('price must be greater than 0. ')

#     return price * tax
#     print(calculate_final_price)

# total = calculate_final_price(float(input('what is the price: ')), .5)
# print(total)



# num = .99

# if 0 <= num < 1:
#     print('I am between 0 and 1')
