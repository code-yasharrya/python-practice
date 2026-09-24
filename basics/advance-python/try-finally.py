def main():
    try:
        a=int(input("hey, enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("i am inside of finally")


main()




# try:
#     a=int(input("hey, enter a number: "))
#     print(a)

# except Exception as e:
#     print(e)

# print("i am in side of finally")
