import pandas as pd

# My Student Dictionary
cooking_class_dict = {"Name":['Sarah', 'Joe', 'Alice'],
                      "Favorite food":['Pizza','IceCream','Mango']}

# What does this look like
students_df = pd.DataFrame(cooking_class_dict)
# print(students_df)

# output
students_df.to_excel('output.xlsx', index=False)


