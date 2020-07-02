class MyClass():
    a = "マイクラス"
    __b = 0
    #mydataの初期値を引数で与える
    def __init__(self, data):
        self.__number = Myclass.__b
        self.mydata = data
        print("MyClass Object is created,number:",self.__number)
        MyClass.__b += 1
    
    def show_number(self):
        print(self.__number)

if __name__ == "__main__":
    print("MyClassのクラス変数 a:", MyClass.a)
    instance1 = MyClass(1)
    instance2 = MyClass(10)
    instance1.show_number()
    instance2.show_number()

    print("mydata of instance1:", instance1.mydata)
    print("mydata of instance2:", instance2.mydata)
    instance1.mydata += 1
    instance2.mydata += 2
    print("mydata of instance1:", instance1.mydata)
    print("mydata of instance2:", instance2.mydata)