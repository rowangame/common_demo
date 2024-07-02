
from cls_sub import CSub
from cls_base import CBase

def test1():
    csub = CSub()

    # 类的所有属性
    print(csub.__dict__)

    # 类的文档说明(注释)
    print(csub.__doc__)

    # 类的所有属性和方法
    print(dir(csub))

    # repr()可以用于输出对象的详细信息，以便帮助识别问题和理解程序的状态
    print(repr(csub))

    # 类名
    print("cls.name:", csub.__class__.__name__)

def test2():
    csub = CSub()
    priV = csub.getPrivateValue()
    pubV = csub.getPublicValue()
    print(priV,pubV)

if __name__ == "__main__":
    test1()
    # test2()
