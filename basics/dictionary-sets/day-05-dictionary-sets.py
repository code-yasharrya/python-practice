# dictionary

d={}

marks={
    "yash":100,
    "karan":85,
    "akshay":85,
    "shivanandam":100,
}

print(marks,type(marks))

print(marks["yash"])


# dictionary methods

marks={
    "yash":100,
    "karan":85,
    "akshay":85,
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"deep":90,"yash":99})
# print(marks)

# print(marks.get("yash9"))
# print(marks["yash6"])
# marks.pop("akshay")
# print(marks)
# marks.popitem()
# print(marks)


# set

e=set() # don't use s={} as it will create an empty dictionary

s={23,45,65,3,3,3,3}

print(s)


# set methods

s={1,2,3,4,5,6}

# print(s,type(s))
# s.add(245)
# print(s,type(s))
# s.remove(4)
# print(s)


# set union intersection

s1={1,2,3,4,5,6}

s2={6,7,8,9,10,6}

print(s1.union(s2))

print(s1.intersection(s2))


# practice code
# 1)
words={
    "madat":"help",
    "khursi":"chair",
    "panka":"fan"
}

word = input("enter the word you want meaning of: ")

print(words[word])

# 2)
s=set()
n=input("enter number one: ")
s.add(int(n))

n=input("enter number two: ")
s.add(int(n))

n=input("enter number three: ")
s.add(int(n))

n=input("enter number four: ")
s.add(int(n))

n=input("enter number five: ")
s.add(int(n))

n=input("enter number five: ")
s.add(int(n))
n=input("enter number five: ")
s.add(int(n))
n=input("enter number five: ")
s.add(int(n))
n=input("enter number five: ")
s.add(int(n))


print(s)

# 3)
s= set()
s.add(18)
s.add("18")
print(s)

# 4)
s= set()
s.add(18)
s.add(18.0)
s.add("18")
print(len(s))

# 5)
s={}
print(type(s))

# 6)
d={}
name= input("enter friends names:")
lang= input("enter language names:")
d.update({name:lang})
name= input("enter friends names:")
lang= input("enter language names:")
d.update({name:lang})
name= input("enter friends names:")
lang= input("enter language names:")
d.update({name:lang})
name= input("enter friends names:")
lang= input("enter language names:")
d.update({name:lang})
print(d)

# 7)
s={3,4,12,"harry",[1,2]}
# set are immutables


