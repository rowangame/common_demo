class MyCls(object):
    number = 10

    def __init__(self, value: int):
        self.value = value
        print('init')

    def __del__(self):
        print('delete')

    def showinfo(self):
        print('name=', self.__class__.__name__)

    def __myfun__(self):
        print('myfun call...')


def testCls():
    clsA = MyCls(1)
    clsB = MyCls(2)
    clsA.number = clsA.number + 3
    print(clsA.number, clsB.number, MyCls.number)
    print(id(clsA.number), id(clsB.number), id(MyCls.number))
    MyCls.number += 5
    print(clsA.number, clsB.number, MyCls.number)
    print(id(clsA.number), id(clsB.number), id(MyCls.number))

    # 设置类的属性
    # print(hasattr(clsA,'b'))
    # #clsA.b = 5
    # setattr(clsA,'b',5)
    # print(hasattr(clsA,'b'))

    # 输出类的信息
    print('clsA info=', str(clsA))
    print('clsA id = %x' % (id(clsA)))


if __name__ == '__main__':
    testCls()
