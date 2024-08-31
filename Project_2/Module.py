'''My import statements to pull functions necessary for calculations'''

from datetime import datetime
import math
import pandas
import csv
import os

# Set local directory for export of txt file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

'''Initialize the class "Employee" to capture the attributes from the Main file and initialize the variables. '''
class Employee(object):

    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    '''Below are the requested Methods to view and manipulate the attribute data'''

    # string representation of the data
    def __str__(self):
        return f'{self.name} {self.job_title} {self.department} {self.salary} {self.hire_year}'
    
    # function to print the total number of years worked in a string. (current date - hire year)
    def years_worked(self):
        print(f'Years worked: {datetime.now().year - self.hire_year}')

    # function to caluculate total expense of employee and return the answer in a string. (years worked * salary)
    def total_expense(self):        
        emp_total_expense = (datetime.now().year - self.hire_year) * self.salary
        return f'Total expense: {(datetime.now().year - self.hire_year) * self.salary}'

    # function to print all of the employee information into a txt file named after said employee (replacing spaces with "_")
    def print_employee_information(self):
        filename = f"{self.name.replace(' ', '_')}.txt"
        with open(filename, 'w') as file:
            file.write(f"Employee Name: {self.name}\n")
            file.write(f"Job Title: {self.job_title}\n")
            file.write(f"Department: {self.department}\n")
            file.write(f"Salary: {self.salary}\n")
            file.write(f"Year Hired: {self.hire_year}\n")
            
    # Accessor methods (getters) for the attributes in the main file
    def get_name(self):
        return self.name

    def get_job_title(self):
        return self.job_title

    def get_department(self):
        return self.department

    def get_salary(self):
        return self.salary

    def get_hire_year(self):
        return self.hire_year 
    

    # Mutator methods (setters) for the attributes in the main file
    def set_name(self, name):
        self.name = name

    def set_job_title(self, job_title):
        self.job_title = job_title
    
    def set_department(self, department):
        self.department = department

    def set_salary(self, salary):
        self.salary = salary

    def set_hire_year(self, hire_year):
        self.hire_year = hire_year
    
    