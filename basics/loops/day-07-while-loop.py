'''1. While Loop:
Condition-based: A while loop runs as long as a specified condition is True.
Use Case: Use a while loop when you don’t know beforehand how many times the loop will run, 
but you want it to keep running until a condition is met or no longer holds true.
'''

i=1
while(i<=51):
    print(i)
    i+=1


# practice code
# 1)
n=int(input("enter the number\n"))
i=1
while(i<11):
    print(f"{n}*{i}={n*i}")
    i+=1
# 2)
n=int(input("enter the number\n"))
i=0
sum=0
while(i<=n):
    sum+=i
    i+=1


print(sum)

# 3)


