class employee:
    company="ITC"
    name="YASH AARYA"
    salary=1200000
    def show(self):
        print(f"the name of the employees {self.name} and the salary is {self.salary}")

class coder:
    language="python"
    def printlanguages(self):
        print(f"out of all the languages here is your language: {self.language} ")


class programmer (employee,coder):
    company="ITC INFOTECH"
    def showlanguage(self):
        print(f"the name is {self.company} and the languages is {self.language}")

a = employee()
b = programmer()

b.show()
b.printlanguages()
b.showlanguage()
