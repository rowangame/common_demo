import math


class MyCls(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class Coordinate:
    x = 10
    y = -5
    z = 0

    @classmethod
    def length(cls):
        return math.sqrt(cls.x * cls.x + cls.y * cls.y + cls.z * cls.z)

    def realLength(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def showinfo(self):
        print('x=%f,y=%f,z=%f' % (self.x, self.y, self.z))


def testFunction():
    # 复数乘法
    cpx1 = complex(1, 2)
    cpx2 = complex(1, 2)
    print(cpx2 * cpx1)

    # 属性判断
    point = Coordinate()
    print(hasattr(point, 'x'))
    print(hasattr(point, 'w'))

    # 静态方法
    print(Coordinate.length())

    p1 = Coordinate()
    p2 = Coordinate()
    p1.showinfo()
    p2.showinfo()
    p2.z = 10
    p1.showinfo()
    p2.showinfo()
    print(p1.realLength())
    print(p2.realLength())
    print(Coordinate.length())

    # 格式化函数
    print("{:.2f}".format(3.1415926))

    # isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
    arg = 123
    print(isinstance(arg, int))  # 输出True
    print(isinstance(arg, str))  # 输出False

    # sum函数
    st = (1, 2, 3, 4, 5)
    print('sum(st)=', sum(st))

    print(dir(MyCls))
    mycls = MyCls()
    print('----->', hasattr(mycls, '_x'), type(mycls._x), type(mycls.x))


    # 首先获得Iterator对象:
    it = iter([1, 2, 3, 4, 5])
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
            print(x)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break


if __name__ == '__main__':
    testFunction()
