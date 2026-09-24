# Introduction of String

name="yash"

nameshort=name[0:3]# start from index 0 all the way till 3 (excluding 3)

print(nameshort)

character= name [0]

print( character)

# Negative Slicing
name="yash"

print(name[0:3])

print(name[-3:-1])

print(name[1:3])

print(name[:4])# is same as print(name[0:4])

print(name[1:])# is same as print(name[1:4])

print(name[1:4])

# String Functions
name="yash"

print(len(name))

print(name.endswith("ash"))

print(name.startswith("yas"))

print(name.capitalize())

# Escape sequence
a="yash is the good boy \n but not \t a \"bad\" boy"

print(a)

#practicing strings

1)
name=input("enter you name:")

print(f"good afternoon {name}")


2)
letter='''dear <|name|>, 

          you are selected!

          <|date|>'''

print(letter.replace("<|name|>","yash").replace(" <|date|>","24 september 2050"))


3) 
name ="yash is a good boy  and  "

print(name.find("  "))


4)
name ="yash is a good boy  and  "

print(name.replace("  ", " "))#string are immutable


5)
letter="dear yash \n this python course is nice.\n thanks"

print(letter)
