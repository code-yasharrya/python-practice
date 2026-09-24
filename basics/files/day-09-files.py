# files python
'''

'''
f=open("file.txt")
data=f.read()
print(data)
f.close()

# files write
lapusachin="kya hai sachin mein lapu sa tho sachin hai"
l=open("lapu.txt","w")
l.write(lapusachin)
l.close()

# more files function

f=open("myfile.txt")
# lines1= f.readline()
# print(lines1,type(lines1))

# lines2= f.readline()
# print(lines2,type(lines2))

# lines3= f.readline()
# print(lines3,type(lines3))

# lines4= f.readline()
# print(lines4,type(lines4))

# lines5= f.readline()
# print(lines5,type(lines5))

# lines6= f.readline()
# print(lines6,type(lines6))

line=f.readline()
while(line != ""):
    print(line)
    line=f.readline()

# file append
lapusachin="kya hai sachin mein lapu sa tho sachin hai"
l=open("lapu.txt","a")
l.write(lapusachin)
l.close()

# with files

f=open("file.txt")
print(f.read())
f.close
# the same can be written using with statement like this:



with open("file.txt")as f:
   print(f.read())

#    you dont have to explicitly close the file



f.close()
