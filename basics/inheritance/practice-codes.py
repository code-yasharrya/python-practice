# 1)
class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,num):
        return self.n+num.n
    

    
n=number(1)
m=number(2)
print(n+m)

# 2)
class animal():
    pass

class pets(animal):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("bao bow !")



a=dog()
a.bark()

# 3)
class employee:
     
     salary=234
     increment=20
     @property
     def salaryafterincrement(self):
          return(self.salary+self.salary*(self.increment/100))
     
     @salaryafterincrement.setter
     def salaryafterincrement(self,salary):
        self.increment=((salary/self.salary)-1)*100







e=employee()
print(e.salaryafterincrement)
e.salaryafterincrement=280.8
print(e.increment)


# 4)
class complex:
    def __init__(self,r,i):
        self. r=r
        self. i=i

    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
    
    def __mul__(self, c2):
        r = self.r * c2.r - self.i * c2.i
        i = self.r * c2.i + self.i * c2.r
        return complex(r,i)

    def __str__(self):
        return f"{self.r} + {self.i}i"
    


c1=complex(1,2)
c2=complex(3,4)
print(c1+c2)
print(c1*c2)


# 5)
class vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        result=vector(self.x + other.x,self.y+ other . y , self.z + other.z)
        return result
    
    def __mul__(self,other):
        result=self.x *+self.y* other . y + self.z * other.z
        return result

    def __str__(self):
        return f"vector({self.x},{self.y},{self.z})"  



v1=vector(3,4,5)
v2=vector(5,6,7)
v3=vector(7,9,8)

print(v1+v2)
print(v1*v2)

print(v1+v3)
print(v1*v3)




# 6)

class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        result=vector(self.x + other.x,self.y+ other . y , self.z + other.z)
        return result
    
    def __mul__(self,other):
        result=self.x *+self.y* other . y + self.z * other.z
        return result

    def __str__(self):
        return f"{self.x}i {self.y}j {self.z}k"  



v1=vector(3,4,5)
v2=vector(5,6,7)
v3=vector(7,9,8)

print(v1+v2)
print(v1*v2)

print(v1+v3)
print(v1*v3)


# 7)
class vector:
    def __init__(self,l):
        self.l=l



    def __len__(self):
        return len(self.l)
    

v1=vector([1,2,3])
print(len(v1))
