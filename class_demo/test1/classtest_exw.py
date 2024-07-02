class MyClass:
    def __init__(self):
        # 公有成员
        self.public_member = 10
        # 私有成员
        self.__private_member = 20

    def public_method(self):
        print("Public method")

    def __private_method(self):
        print("Private method")

    def access_private_member(self):
        # 在类的内部可以访问私有成员
        print("Accessing private member:", self.__private_member)

    def call_private_method(self):
        # 在类的内部可以调用私有方法
        print("Calling private method:")
        self.__private_method()

# 创建对象
obj = MyClass()

# 在类的外部无法直接访问私有成员和私有方法
# 以下行将引发 AttributeError
# print(obj.__private_member)
# obj.__private_method()

# 但是可以通过公有方法来访问私有成员和调用私有方法
obj.access_private_member()
obj.call_private_method()

# 公有成员和方法可以直接访问
print(obj.public_member)
obj.public_method()