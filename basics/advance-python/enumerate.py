l=[1,3243,53,2,34,24]

# index=0
# for item in l:
#     print(f"the item number at index {index} is {item}")
#     index += 1

# this can be simplified using enumerate function

for index ,item in enumerate(l):
    print(f"the item number at index {index} is {item}")

