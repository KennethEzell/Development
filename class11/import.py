import os
import pandas as pd

# print("my current working directory", os.getcwd())

# os.chdir ("C:\SUMMER-2024-PROGRAMMING-CONCEPTS\class11_list_pt2")
# print('my lists part 2 folder has a new cmd', os.getcwd())

baseline = pd.read_csv('emails.csv')

# print(baseline)

baseline['uni-id'] = baseline['uni-id'] + '@gmail.com'

# print(baseline)

baseline.to_excel('output.xlsx', index=False)