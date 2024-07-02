# -*- coding: UTF-8 -*-
import sys


def testEval():
    strEqal = '1*2*3*4+(8+2)**3'
    print(eval(strEqal))


def testList():
    # 列表元素可修改，可删除等
    print('--------testList--------')
    # lst = [1,2,3]
    lst = list()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(lst)
    lst.remove(1)
    print(lst)


def testSet():
    # 集合三特性: 1:确定性 2:互异性 3:无序性
    print('--------testSet--------')
    st = set()
    st.add(1)
    st.add(2)
    st.add(3)
    print(st)


def testTuple():
    # 元组元素不能删除, 元素值不能修改
    print('--------testTuple--------')
    tp = (1, 2, 3)
    print(tp)


def testDict():
    # 字典由键值对构成
    print('--------testDict--------')
    dt = dict()
    index = 0
    for i in 'python':
        dt[index] = i
        index = index + 1
    print(dt)

    print(dt.items())
    dt.pop(0)
    print(dt)

    for k in dt:
        print('k,v=', k, dt[k])


def testBase():
    # for i in (1,2,3,4,5,6):
    #     a = 1 + 2
    #     print('i=%d id=%d' % (i,id(a)))

    a = 1
    print("id1", id(a))
    a = 10
    print("id2", id(a))
    a = 1
    print("id3", id(a))


def testEqual():
    # 比较列表元素内容
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print(id(lst1), id(lst2), lst1 == lst2)

    lsta = ['a', 'b', 'c']
    lstb = [chr(97), 'b', 'c']
    print(id(lsta), id(lstb), lsta == lstb)


def testAscii():
    hexstr = '55 AA 04 03 CC'
    data = bytes.fromhex(hexstr)
    rlt = data.hex()
    print(repr(data))
    print(rlt)

    # '5' = 53 '0' = 48 ' ' = 32
    binData = b'55 AA 04 03 CC'
    print(type(binData), len(binData))
    for i in binData:
        print(i, chr(i))


def testForSenior():
    for modname, minver in [
        ("cycler", "0.10"),
        ("dateutil", "2.7"),
        ("kiwisolver", "1.0.1"),
        ("numpy", "1.16"),
        ("pyparsing", "2.2.1"),
    ]:
        print(modname, minver)


def testBytes():
    try:
        b1 = bytes.fromhex('01 a0 03')
        print(b1)
        for tmpV in b1:
            print(tmpV)

        str = '%03d' % 1
        print(str)
    except Exception as e:
        print(repr(e))


def testFormat():
    try:
        v1 = {'key1': 'v1', 'key2': 'v2', 'key3': 'v3'}
        sinfo = '%(key1)s, %(key3)s, %(key2)s' % v1
        print(sinfo)
    except Exception as e:
        print(repr(e))


def testTupleEx():
    t1 = ('v11', 'v22', 'v33', 'v44', 'v55')
    print(f'len={len(t1)}')
    v1,v2,v3 = t1[:3]
    print(v1, v2, v3)


class MyInfo():
    def __init__(self):
        self.atrA = None
        self.strA = ''

def testNone():
    myinfo = MyInfo()
    # print(dir(myinfo))
    print(type(myinfo.atrA))
    print(type(myinfo.strA))
    # == 是比较两个对象的内容是否相等，即两个对象的“值“”是否相等，不管两者在内存中的引用地址是否一样
    if myinfo.atrA == None:
        print('is none  11')
    else:
        print('not none 11')

    # is 比较的是两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同。即is比较两个条件：1.内容相同。2.内存中地址相同
    if myinfo.atrA is None:
        print('is none 22')
    else:
        print('not none 22')

    '''
    print('1', type(myinfo.atrA), id(myinfo.atrA))
    print('2', type(3) == int)
    print('3', type(myinfo) == MyInfo)
    print('4', type([]) == list)
    print('5', type(()) == tuple)
    print('6', type({'a':1,'b':2}) == dict)
    print('7', type('') == str)
    print('8', type({1,2,3}))
    print('id(None)', id(None))

    v1 = (4, 10)
    v2 = (4, 10)
    print('test', id(v1), id(v2), v1 >= v2)
    '''

    # # AttributeError: 'MyInfo' object has no attribute 's1'
    # if myinfo.s1 == None:
    #     print()

    print('1', isinstance(3, int))
    print('2', isinstance({1,2,3}, set))
    print('3', 'NoneType' in str(type(None)))
    print('经验证None 是 NoneType类的实例。\n 但3.7版Python 不能导入type.NoneType。Python版本需要 >=3.10 \n 才能导入成功')


if __name__ == '__main__':
    # testList()
    # testSet()
    # testTuple()
    # testDict()
    # testBase()
    # testEqual()
    # testAscii()
    # testEval()
    # testForSenior()
    # testBytes()
    # testFormat()
    # testTupleEx()
    testNone()