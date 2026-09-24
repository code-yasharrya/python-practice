# list

friend=["apple","orange",5,345.06,"akash","rohan"]

print(friend[0])

friend[0]="mango"#unlike strings lists are mutable

print(friend[0])


# list methods

# adding value at the end 
# friend=["apple","orange",5,345.06,"akash","rohan"] 
# print(friend) 
# friend.append("yash aarya") 
# print(friend) 
 
#sorting 
l1=[43,24,65,86,3658,47] 
# l1.sort() 
# l1.reverse() 
# l1.insert(3,"yash") 
# l1.append([3,34,"yash"]) 
# l1.extend([3,34,"yash"]) 
# # value=l1.pop(3) 
# print(value) 
# l1.remove(43) 
print(l1) 


# tuple

a = (1,45,342,"yash","rohan","shivam" )

print(a)

print(type(a))


# tuple methods

a = (1,45,45,342,"yash","rohan","shivam" )
# print(a)
# print(type(a))
# no=a.count(45)
# print(no)
i=a.index(45)
print(i)
# print(len(a))
# a=(1,2,3,4)
# print(7 in a)
# print(len(a))


# practice codes

fruits=[]

f1=input("enter fruit name:")

fruits.append(f1)

f2=input("enter fruit name:")

fruits.append(f2)

f3=input("enter fruit name:")

fruits.append(f3)

f4=input("enter fruit name:")

fruits.append(f4)

f5=input("enter fruit name:")

fruits.append(f5)

f6=input("enter fruit name:")

fruits.append(f6)

f7=input("enter fruit name:")

fruits.append(f7)

print(fruits)


marks=[]

f1=int(input("enter marks here:"))

marks.append(f1)

f2=int(input("enter marks here:"))

marks.append(f2)

f3=int(input("enter marks here:"))

marks.append(f3)

f4=int(input("enter marks here:"))

marks.append(f4)

f5=int(input("enter marks here:"))

marks.append(f5)

f6=int(input("enter marks here:"))

marks.append(f6)


marks.sort()

print(marks)


a=(36,52,2345)

a[1]="yash"

print(a)


a=(2,5,5,2)

print(sum(a))


a=(2,5,5,2,0,0,0)

n=a.count(0)

print(n)
