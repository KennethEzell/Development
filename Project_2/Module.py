




class Employee(object):

    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    def __str__(self):
        return f'{self.name} {self.job_title} {self.department} {self.salary} {self.hire_year}'
    