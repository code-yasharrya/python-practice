class employee:
    def __init__(self):
        print("constructor of the employee")
    a=1
class programmer (employee):
    def __init__(self):
        print("constructor of the programmer")
    b=2
class manager (programmer):
    def __init__(self):
        super().__init__()
        print("constructor of the manager")
    c=3
o=employee()
print(o.a) # print the a attribute
# print(o.b) # show an error as there is no b attribute in employee class
o=programmer()
print(o.a,o.b)
o=manager()
print(o.a,o.b,o.c)
