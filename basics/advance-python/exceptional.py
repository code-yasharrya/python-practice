try:
    a=int(input("hey buddy enter a number please: "))
    print(a)

except ValueError as v:
    print("please enter the value in number not in words")
    
except Exception as e:
    print(e)
print("thank you for trying")
