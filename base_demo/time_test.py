import calendar
import math
import time


def testTime():
    print(time.time())

    localtime = time.localtime(time.time())
    print(localtime)
    # 格式化日期
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

    # 获取某月日历
    cal = calendar.month(2021, 5)
    print(type(cal))
    print(cal)


def testTimeEx():
    # for i in range(1,2,1):
    #     #print('i=%d' % (i))
    #     #print(time.time_ns())
    #     print(time.time(),time.time_ns())
    #
    # timeSecs = 1620699077.9471
    # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timeSecs)))

    lasttick = time.time()
    a = 1
    for i in range(1000000):
        a += 1
    detime = time.time() - lasttick
    print('用时%f(s)或%d(ms)' % (detime, math.trunc(detime * 1000)))


if __name__ == '__main__':
    testTime()
    # testTimeEx()
