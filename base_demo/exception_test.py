import math
import time
import traceback


def addex(a, b):
    if b < 0:
        raise ValueError("b value must big than zero")
    print("this call...", a + b)
    return a + b


def testRaiseCase():
    try:
        num = addex(1, -1)
        print(num)
    except Exception as e:
        print(repr(e))


def testException():
    try:
        num = 1 / 0
    except Exception as e:
        print(str(e))
        # 输出异常详细信息
        # traceback.print_exc()
    else:
        print('success')


def testFinally():
    st = dict()
    try:
        t1 = time.time()
        st['t1'] = t1
        num = 1 / 0
    except Exception as e:
        t2 = time.time()
        st['t2'] = t2
        print('error:', str(e))
        # traceback.print_exc()
    else:
        t3 = time.time()
        st['t3'] = t3
        print('没有出错时的执行语句')
    finally:
        t4 = time.time()
        st['t4'] = t4
        print('始终执行的语句')
    print(st)


def testTimeAccuracy():
    l = []
    for i in range(100):
        t1 = time.time()
        for j in range(1000 * 100):
            a = 1 + 2
        t2 = time.time()
        dtime = t2 - t1
        l.append(math.trunc(dtime * 1000))
    print(l)


def testTrunc():
    v = math.trunc(3.534)
    print("v=", v)


if __name__ == '__main__':
    # testException()
    # testFinally()
    testRaiseCase()
    # testTimeAccuracy()
    testTrunc()