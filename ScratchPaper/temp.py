# def verify_num(user_num = input("Enter a number: ")):
#     while True:
#         if user_num == float(user_num):
#             return user_num
#         else:
#             print("Invalid input. Please enter a valid number.")



sum = 0
count = 0
# while True:
#     x = input('Enter a number: ')
#     if float(x):
#         for i in range(10,x,5):
#             sum += i
#             count += 1
#             print(sum)
#         else:
#             print("Invalid input. Please enter a valid number. ")
#         print(sum/count)

def valid_num(x="Enter a number: "):
    while True:
        userin = input(x)
        try:
            userin = int(userin) 
            return userin
            break
        except ValueError:
                print("Invalid input. Please enter a valid number. ")
     
x = valid_num()
sum = 0
count = 0    

for i in range(10,x,5):
    sum += i
    count += 1
    print(sum)
print(sum/count)       
              



# while True:
#     sum = 0
#     count = 0    
#     try:
#         x = int(input('Enter a number: '))          
#         for i in range(10,x,5):
#             sum += i
#             count += 1
#             print(sum)
#         print(sum/count)       
#         break 
#     except ValueError:
#         print("Invalid inpu. Please enter a valid number. ")    

