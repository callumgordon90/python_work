

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise = 5000):
        self.annual_salary = int(self.annual_salary) + salary_raise

        return(self.annual_salary)

cally = Employee("callum", "gordon", 400)

print(f"cally salary: {cally.annual_salary}")

cally.give_raise(1)

print(f"new cally salary: {cally.annual_salary}")