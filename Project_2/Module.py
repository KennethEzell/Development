

from datetime import datetime
import math
import pandas
import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Employee(object):

    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    def __str__(self):
        return f'{self.name} {self.job_title} {self.department} {self.salary} {self.hire_year}'
    
    def years_worked(self):
        print(f'Years worked: {datetime.now().year - self.hire_year}')

    def total_expense(self):        
        emp_total_expense = (datetime.now().year - self.hire_year) * self.salary
        return f'Total expense: {(datetime.now().year - self.hire_year) * self.salary}'

    def print_employee_information(self):
        filename = f"{self.name.replace(' ', '_')}.txt"
        with open(filename, 'w') as file:
            file.write(f"Employee Name: {self.name}\n")
            file.write(f"Job Title: {self.job_title}\n")
            file.write(f"Department: {self.department}\n")
            file.write(f"Salary: {self.salary}\n")
            file.write(f"Year Hired: {self.hire_year}\n")
            

    # Accessor methods (getters)
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
    

    # Mutator methods (setters)
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
    
    


    # def set_job_title(self, job_title):
    #     if isinstance(job_title, str):
    #         self._job_title = job_title
    #     else:
    #         raise ValueError("Job title must be a string.")

    # def set_department(self, department):
    #     if isinstance(department, str):
    #         self._department = department
    #     else:
    #         raise ValueError("Department must be a string.")

    # def set_salary(self, salary):
    #     if isinstance(salary, (int, float)) and salary >= 0:
    #         self._salary = float(salary)
    #     else:
    #         raise ValueError("Salary must be a non-negative number.")

    # def set_hire_year(self, hire_year):
    #     if isinstance(hire_year, int) and hire_year > 0:
    #         self._hire_year = hire_year
    #     else:
    #         raise ValueError("Hire year must be a positive integer.")

# with open('animals.txt', 'w') as file:
#     file.writelines(animals)


# df = pd.DataFrame.from_dict(data)

# df.to_csv('output.csv', index=False)