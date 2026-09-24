# for loops

'''Use Case: Use a for loop when you have a predefined range or iterable and
 you want to loop through it a specific number of times.'''
print(1)
print(1)
print(1)
print(1)
print(1)

# the same task  can be done like this:
for i in range(1,6):
    print(i)
# 2)
for i in range(4):
    print(i)

# for loops iterates
# for loop with list
l=[12,12,233,2434,556]
for i in l:
    print(i)
#  for loop with tuple
t=(122,234,45,75,864,8,57)
for i in t:
    print(i)

#for loop with string
s="yashaarya"
for i in s:
    print(i)
  
# for loop with else
l=[1,23,4,]

for item in l:
    print(item)

else:
    print("done") # this printed when the loop exhausts!
  
# for with break and continue 
for i in range(100):
    if(i == 34):
        break # exit the loop right now
    print(i)


for i in range(100):
    if(i == 34):
        continue # skip this iteration
    print(i)


# for loop with pass

for i in range(645):
    pass

i=0
while(i<45):
    print(i)
    i+=1

# practice code

# 1)
n=int(input("enter the number\n"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

# 2)
l = ("yash","yashwant","yashoda","karan","jigra")
for name in l:
    if(name.startswith("j")):
        print(f"hellow {name}")
# 3)
n=int(input("enter the number\n"))

for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break

else:
    print("number is prime")

# 4)
n=int(input("enter the number\n"))
product=1
for i in range(1, n+1):
    product=product*i
print(f"the factorial of {n} is {product}")

# 5)
n=int(input("enter the number\n"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")
 
 # 6)
n=int(input("enter the number\n"))
for i in range(1,n+1):
    print("*"*i,end="")
    print("")
 # 7)
n=int(input("enter the number\n"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")
 
 # 8)

n=int(input("enter the number\n"))
for i in range(1,11):
    print(f"{n}*{11-i}={n*(11-i)}")
 
