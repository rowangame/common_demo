
class CBase(object):
    def __init__(self):
        super(CBase, self).__init__()
        print("CBase.__init__\n")
        self.__priV = 1
        self.pubV = 2

    def __new__(cls, *args, **kwargs):
        print("CBase.__new__\n")
        return super().__new__(cls)
    
    def __del__(self):
        print("CBase.__del__\n")

    def getPrivateValue(self):
        return self.__priV

    def getPublicValue(self):
        return self.pubV

    def __privateMethod(self):
        print("__privateMethod...\n")

    def publicMethod(self):
        print("publicMethod...\n")
        self.__privateMethod()