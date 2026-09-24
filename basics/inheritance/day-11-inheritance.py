class employee:
    company="ITC"
    def show(self):
        print(f"the name of the employees {self.name} and the salary is {self.salary}")

class coder:
    language="python"
    def printlanguages(self):
        print(f"out of all the languages here is your language: {self.language} ")


class programmer:
    company="ITC INFOTECH"
    def show(employee , coder):
        print(f"the name is {employee.name} and the salary is {employee.salary}")


    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language}")


a = employee()
b = programmer()

print(a.company , b.company)
