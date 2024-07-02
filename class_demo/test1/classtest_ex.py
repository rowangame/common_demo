
class Parent:
    pA: int = 0
    pB: int = 1

    @classmethod
    def showInfo(cls):
        print("")
        print("Parent.showInfo")
        print(f"id(pA)={id(cls.pA)},id(pB)={id(cls.pB)}")
        print("pA=%d pB=%d" % (cls.pA, cls.pB))

    def doSomething(self):
        print("ClsBase.doSomething")

class Child(Parent):
    def __init__(self):
        print(id(self), id(Parent))
        super(Child, self).__init__()
        self.showInfo()
        self.__a = 10
        self.__b = 11

    def __del__(self):
        print("delete...")

    def setValue(self, vA, vB: int):
        self.pA = vA
        self.pB = vB
        # self.pC = vA + vB

    def showInfo(self):
        print("")
        print("ClsChild.showInfo")
        print(f"id(pA)={id(self.pA)},id(pB)={id(self.pB)}")
        print("pA=%d pB=%d" % (self.pA, self.pB))

    def doSomething(self):
        print("ClsChild.doSomething")

    def privateAccessMember(self):
        print("privateAccessMember:", self.__a)


if __name__ == "__main__":
    try:
        objC = Child()
        objC.doSomething()
        objC.showInfo()

        objC.setValue(3, 4)
        objC.showInfo()
        # objC.pC = objC.pA + objC.pB
        setattr(objC, "pC", objC.pA + objC.pB)
        print(objC.pC)
        # print(objC.__a)
        objC.privateAccessMember()

        Parent.showInfo()
        Parent.pA = -1
        Parent.pB = -2
        Parent.showInfo()
        objC.showInfo()
    except Exception as e:
        print(repr(e))