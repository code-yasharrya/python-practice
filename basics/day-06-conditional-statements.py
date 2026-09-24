# conditional statement

# if else statement

a= int(input("enter your age"))

if(a>18):
    print("you above the age of consent")
else:
    print("you are below the age of consent")
    
    
print("you are genius")


# if elif else ladder

a= int(input("enter your age"))

if(a>=18):
    print("you above the age of consent")
elif(a<=0):
    print("you are entering an invalid age")
else:
    print("you are below the age of consent")
    
    
print("you are genius")


# quize

a=int(input("enter an age"))

if(a>=18):
    print("yes")
else:
    print("no")


# multiple if statement

a= int(input("enter your age"))

# if statement no:1

if(a%2 == 0):
    print("the value you entered is even")
else:
    print("the value you entered is odd")

# end of if statement no:1


# if statement no:2

if(a>=18):
    print("you above the age of consent")
elif(a<=0):
    print("you are entering an invalid age")
else:
    print("you are below the age of consent")

# end of if statement no:2
    
print("you are genius")


# practice problems
# 1)
a1=int(input("enter the number"))

a2=int(input("enter the number"))

a3=int(input("enter the number"))

a4=int(input("enter the number"))

if(a1>a2 and a1>a3 and a1>a4):
    print("greatest number is a1:",a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("greatest number is a2:",a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("greatest number is a3:",a3)

else:
    print("greatest number is a4:",a4)
# 2)
marks1 = int(input("enter the marks 1:"))
marks2 = int(input("enter the marks 2:"))
marks3 = int(input("enter the marks 3:"))

# check for total persontage

total_persontage = (100*(marks1 + marks2 + marks3))/300

if(total_persontage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are fucking genius" , total_persontage)
else:
    print("you are fucking loser",total_persontage)

 # 3)
  p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click on this"

message=input("inter your comment: ")
if((p1 in message) or(p2 in message)or(p3 in message) or (p4 in message)):
    print("this a spam")
else:
    print("this is not a spam")

# 4)  
username=input("enter user name")

if(len(username)<=10):
    print("your user name contain less than 10 character")

else:
    print("your user name contain more than 10 character")
  
# 5)
l=["yash","roshan","yash2","yash3"]
name=input("enter the name\n")
if(name in l):
    print("your name in the list")
else:
    print("your name not in the list")
# 6)
marks=int(input("enter the marks:"))

if(marks<=100 and marks>=90):
    grade="ex"
elif(marks < 90 and marks>=80):
    grade="A"
elif(marks < 80 and marks>=70):
    grade="B"
elif(marks < 70 and marks>=60):
    grade="C"
elif(marks < 60 and marks>=50):
    grade="D"
elif(marks < 50):
    grade="F"
    
print("your grade is:",grade)
  
  
# 7)
post=input("enter the post:")

if("yash". lower() in post.lower()):
    print("they are talking about yash")
   

else:
    print("they are not talking about yash")
  
