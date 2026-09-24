# a=int(input("enter your number:"))
# b=int(input("enter your number:"))
# c=int(input("enter your number:"))
# average=(a+b+c)/3
# print(average)




# function definition
def avg():
    a=int(input("enter your number:"))
    b=int(input("enter your number:"))
    c=int(input("enter your number:"))
    average=(a+b+c)/3
    print(average)



avg()    #function call
print("thank  you!")
# avg()
# print("thank  you!")
# avg()
# print("thank  you!")
# avg()
# avg()

# user define function
def goodday():
    name=input("enter your name:")
    print(f"goodday,{name}")

goodday()

# fuction with argument

def goodday(name, ending,middle):
    print("goodday," + name)
    print(ending)
    print(middle)
    return"ok"


a=goodday("yash" ,"you done great job", "thank you")
print(a)
# goodday("karan" ,"you done great job"," thank you")
# goodday("akshay" ,"you done great job"," thank you")
# goodday("shivanandam"  ,"you done great job"," thanks")


# default argument
def goodDay(name,ending="thank you"):
    print(f"goodDay,{name}")
    print(ending)



goodDay("yash","thanks")
goodDay("AARYA")

# recurtion
def factorial(n):
    if(n==1) or (n==0):
        return 1
    return n * factorial(n-1)

n=int(input("enter the number"))
print(f"the factorial of this number: {factorial (n)}")
    
