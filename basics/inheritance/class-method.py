class employee():
    a=1
    @classmethod
    def show(cls):
        print(f"the class attribute of the a is {cls.a}")


ao=employee()
ao.a=34
ao.show()
