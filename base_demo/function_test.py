import time
from functools import lru_cache


def step(n):
    if n <= 1:
        return 1
    else:
        return n * step(n - 1)


# Python functools模块应用于高阶函数，即参数或返回值作为其他函数的函数。
# 函数缓存装饰器lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n == 1:
        return 1
    else:
        if n == 2:
            return 1
    return fib(n - 1) + fib(n - 2)


def fibex(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def myfun(a: int, b: int, c: int = 10):
    return a + b + c


if __name__ == '__main__':
    print(step(n=10))
    print(myfun(1, 2))
    print(myfun(1, 2, 10))

    depth = 500
    times = 10000
    # fib(500),次数:10000 总用时纳秒:12016700
    # 1,1,2,3,5,8,13,21,34,55
    # totalTime = 0
    # for i in range(times):
    #     lasttick = time.time_ns()
    #     fib(depth)
    #     dtime = time.time_ns() - lasttick
    #     totalTime += dtime
    # print('fib(%d),次数:%d 总用时纳秒:%d' % (depth,times,totalTime))

    # fibex(500),次数:10000 总用时纳秒:23032100
    totalTime = 0
    for i in range(times):
        lasttick = time.time_ns()
        fibex(depth)
        dtime = time.time_ns() - lasttick
        totalTime += dtime
    print('fibex(%d),次数:%d 总用时纳秒:%d' % (depth, times, totalTime))
    # 分析结果：函数缓存装饰器后运行速度更快
