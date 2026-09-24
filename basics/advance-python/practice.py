# 1)
''' write a program to open  three files 1.txt 2.txt and 3.txt if any these  files are not present , a massage without
exiting the program must be printed prompting the same.
'''

try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

finally:
    print("thank you so much baby")

# 2)
"""
write program to print third , fifth and seventh element from a list using enumerate function
"""
l=[1,2,3,4,5,6,7,8]
for i,item in enumerate(l):
    if i == 2 or i==4 or i == 6:
        print(item)
# 3)
"""
write a list comprehension to print a list which contains the multiplication table of a user entered number
"""
n = int(input("enter the number which you want: "))
table = [n*i for i in range(1,11)]
print(table)

# 4)
"""  
write a program to display a/b where a and b are integers. if b=0, display infinite by handling the "zeroDivisionerror"
"""

try:
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")


# 5)
"""  
write a program to display a/b where a and b are integers. if b=0, display infinite by handling the "zeroDivisionerror"
"""

try:
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")
