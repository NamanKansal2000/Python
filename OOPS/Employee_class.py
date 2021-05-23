# import datetime


class Employee:

    # Class variables that that will remain constant for all the instances
    no_of_emps = 0
    amount_paid = 0
    raise_pay = 1.04

    # initial fxn that will always run a instance(emloyee input)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.no_of_emps += 1
        Employee.amount_paid += self.pay

    # returns the fullname of the emloyee given the initial information
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Returns the amount paid to the employee after raising
    def pay_raise(self):
        self.pay = (self.pay * self.raise_pay)

    # A Class Method is defined that runs before any instance variable that is
    # before __init__() function also

    # raise the money percentage globally
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_pay = amount

    # To separate the first, last name and pay from a given string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # staticmethod is used if class/instance in not in fuction i.e. it behaves
    # like normal function without any specific call in class
    @staticmethod
    def is_weekday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        else:
            return True

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    # getter is made if we want to use a method as attribute
    # in this case suppose a persons first and last name the email will be
    # updated on its own
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    # Setter is used to assign a value to already existing attribute
    # @fullname.setter
    # def fullname(self, name):
    #     first, last = name.split(' ')
    #     self.first = first
    #     self.last = last


class Developer(Employee):
    raise_pay = 1.07

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Managers(Employee):
    raise_pay = 1.1

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, empl):
        if empl not in self.employees:
            self.employees.append(empl)

    def remove_emp(self, empl):
        if empl in self.employees:
            self.employees.remove(empl)

    def print_emp(self):
        for emp in self.employees:
            print('--> ', emp.fullname())


# Employee info
dev_1 = Developer('Naman', 'Kansal', 500000, 'Python')
emp_1 = Employee('Kunal', 'Kansal', 400000)
emp_1.first = 'Jim'
# emp_1.fullname = 'Himanshu Kansal'
# Report Generated
print(emp_1.fullname())
print(emp_1.email)
print(emp_1.first)
print('No of Employees in company: ', Employee.no_of_emps)
