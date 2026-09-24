class employee: 
    language="python" 
    salary = 1200000
    def __init__(self,name,salary,language): # dunder method which is automatically called
        print("i am creating a object")
        self.name= name
        self.salary = salary
        self.language = language
    
    def getinfo(self):
        print(f"the language is {self.language}\nyour salary is {self.salary}\n")
    @staticmethod
    def greet():
        print("good morning yash sir")

yash = employee("karan\n", 1300000 ,"javascript \n")
print(yash.name,yash.salary,yash.language)
