from Module import Employee

emp1 = Employee('Kenneth Ezell', 'Analyst', 'Transportation', 100000, 2010)
# print(emp1)
# emp1.years_worked()
# print(emp1.total_expense())
# emp1.print_employee_information()
print(emp1.get_name(), emp1.get_job_title(), emp1.get_department(), emp1.get_salary(), emp1.get_hire_year())
emp1.set_name('Chris')
print(emp1.name)
emp1.set_job_title('Buster')
emp1.set_salary(200000)

print(emp1.get_name(), emp1.get_job_title(), emp1.get_department(), emp1.get_salary(), emp1.get_hire_year())