# -*- coding: UTF-8 -*-
# 给类添加多个函数属性

class MyTestCase(object):
    times = 0

    def __init__(self):
        print('__init__')

    @staticmethod
    def getTestFunc(i):
        def test_logic(obj: MyTestCase, value: int):
            print(f'id(obj)={id(obj)}')
            print(f'value={value}')
        return test_logic

    def sum(self, a, b):
        return a + b

    @staticmethod
    def sumEx(a: int, b:int):
        return a + b


def getTestFuncEx(index: int):
    def test_logic(b1: MyTestCase, tag: str, obj: MyTestCase, value: int):
        print(f'id(obj)={id(obj)}')
        print(f'str={tag} value={value}')
    return test_logic


def __generateTestCases():
    for i in range(5):
        name = '%03d' % i
        setattr(MyTestCase, 'test_%s' % name, getTestFuncEx(i))


__generateTestCases()

mtc = MyTestCase()
print('dir(mtc)=', dir(mtc))

# print(id(mtc.test_000))
# print(id(mtc.test_001))
# print(id(mtc.test_002))

print('id(mtc)=', id(mtc))
mtc.test_002(tag='test', obj=mtc, value=1)

total = mtc.sum(1, 2)
print(f'total={total}')

total = MyTestCase.sumEx(2, 3)
print(f'total={total}')