class Employees:
    def __init__(self, name, age, country):
     self.name = name
     self.age = age
     self.country = country

    def get_info(self):
     return f' {self.name}, {self.age}, {self.country}'

empl1 = Employees('Aidana', 44, 'KG')
print(empl1.get_info())  # 'Aidana', 44, 'KG'

class Manager(Employees):
    def __init__(self, name, age, country, departament):
        super().__init__(name, age, country)
        self.departament = departament
    def get_info(self):
     return f' {self.name}, {self.age}, {self.country} {self.departament}'

    def check_dep(self):
        if self.departament == "IT":
            return 'Cool'
        else:
            return 'No cool'


manag1 = Manager('Asel', 22, 'KZ', 'IT')
print(manag1.get_info()) #'Asel', 22, 'KZ', 'IT'
print(manag1.check_dep())

class Intern(Manager):
    def __init__(self, name, age, country, departament, salary, experiance):
        super().__init__(name, age, country, departament)
        self.salary = salary
        self.experiance = experiance

    def get_info(self):
     return f' {self.name}, {self.age}, {self.country} {self.departament}, {self.salary}, {self.experiance}'

    def total_salary(self):
        return f'{self.experiance * 12 * self.salary }  '

intern1 = Intern('Bektur', 22, 'USA', 'IT', 45000, 3)
print(intern1.get_info())  # 'Bektur', 22, 'USA', 'IT', 45000, 3
print(intern1.check_dep())  # Cool
print(intern1.total_salary())  # 1 620 000 som
