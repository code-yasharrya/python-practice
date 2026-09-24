# 1)
class programmer:
    company= "microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
    @staticmethod
    def que():
        print("hey mr give  your introduction first")

    def getinfo(self):
        print(f"my name is {self.name} \n and the company name that i working with is {self.company} \n and my annual packege is {self.salary} \n and my address pin code is {self.pin}")
yash=programmer("yash" ,2000000, 421505)
# print(yash.name,yash.salary,yash.company,yash.pin)
# print(yash.name,yash.company,yash.salary,yash.pin)
k=programmer("karan" ,1500000, 421505)
# print(k.name,k.salary,k.company,k.pin)
yash.que()
yash.getinfo()
k.que()
k.getinfo()

# 2)
class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the squre of this number is  {self.n* self.n}")

    def cube(self):
        print(f"the cube of this number is  {self.n* self.n*self.n}")

    def squareroot(self):
        print(f"the squre root of this number is  {self. n**0.5}")

a=calculator(16)
a.square()
a.cube()
a.squareroot()
    

# 3)
class demo:
    a=4
o=demo()
print(o.a)# print the class attribute because instance attribute is not present
o.a=0 # instance atrribute is set
print(o.a) # print the instance attribute because instance attribute is present
print(demo.a)# print the class atrribute


# 4)
class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the squre of this number is  {self.n* self.n}")

    def cube(self):
        print(f"the cube of this number is  {self.n* self.n*self.n}")

    def squareroot(self):
        print(f"the squre root of this number is  {self. n**0.5}")
    @staticmethod
    def hellow():
        print("hellow yash the best")

a=calculator(25)
a.hellow()
a.square()
a.cube()
a.squareroot()
    


# 5)
from random import randint


class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getstatus(self,):
       print(f" train no: {self.trainNo} is running on time")

    def getfare(self,fro,to):
        print(f"ticket fare is in train no: {self.trainNo} from {fro} to {to} is {randint(250,5000)}")

    def coach(self):
        print(f"your coach no is {randint(1,15)}")

    def seatno(self):
        print(f"your seat no is {randint(1,60)}")


y=train(12971)
y.book("goa","mumbai")
y.getstatus()
y.coach()
y.seatno()
y.getfare("goa","mumbai")


# 6)
from random import randint


class train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo

    def book(self,fro,to):
        print(f"ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getstatus(self,):
       print(f" train no: {self.trainNo} is running on time")

    def getfare(self,fro,to):
        print(f"ticket fare is in train no: {self.trainNo} from {fro} to {to} is {randint(250,5000)}")

    def coach(self):
        print(f"your coach no is {randint(1,15)}")

    def seatno(self):
        print(f"your seat no is {randint(1,60)}")


y=train(12971)
y.book("mumbai","goa")
y.getstatus()
y.coach()
y.seatno()
y.getfare("mumbai","goa")

