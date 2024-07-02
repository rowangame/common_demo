# 定义一个全局变量
mynum = 1


def mysum(a, b):
    return a + b


def myminus(a, b):
    return a - b


def times(a, b):
    return a * b


def testGlobal():
    # 这里要声明全局变量
    global mynum
    mynum = mynum + 1
    print('mynum', mynum)
