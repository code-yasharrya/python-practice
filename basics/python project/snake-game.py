import random
'''
1 for snake 
-1 for water
0 for gun
'''
computer= random.choice([-1,0,1])
# youstr=input("enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

while True:
    youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
    if youstr in youDict:
        break
    else:
        print("Invalid input! Please enter 's', 'w', or 'g'.")
you = youDict[youstr]

print(f" you chose:  {reversedict[you]}\ncomputer chose: {reversedict[computer]}")

if(computer==you):
    print("it a draw")
else:
 if(computer==-1 and you ==1):
    print("you win")
 elif(computer ==-1 and you==0):
    print("you lose!")

 elif(computer==1 and you ==-1):
    print("you lose")
 elif(computer ==1 and you==0):
    print("you win!")
 elif(computer==0 and you ==-1):
    print("you win")
 elif(computer ==0 and you==1):
    print("you lose!")
 else:
      print("something went wrong!")
