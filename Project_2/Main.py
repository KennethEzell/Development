from Module import Employee

# establish values to the attributes for the Module file
emp1 = Employee('Kenneth Ezell', 'Analyst', 'Transportation', 100000, 2010)
print(emp1)

# test years worked function
emp1.years_worked()

# test total expense function
print(emp1.total_expense())

# test print employee information function output to txt file in employee's name
emp1.print_employee_information()

# test accessor functions for data. I placed all of them into one print statement since they are only accessors
print(emp1.get_name(), emp1.get_job_title(), emp1.get_department(), emp1.get_salary(), emp1.get_hire_year())

# below are the mutator functions to change the data attributes
emp1.set_name('Rebecca Ezell')
emp1.set_job_title('Queen of the House')
emp1.set_department('House Affairs')
emp1.set_salary(120000)
emp1.set_hire_year(2006)

# display updated data from the mutator functions
print(emp1)

# create new txt file in new employee name and info
emp1.print_employee_information()


