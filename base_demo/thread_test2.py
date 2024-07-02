# Python中线程的使用（停止操作）
#
# 模块并没有提供暂停, 恢复和停止线程的方法, 一旦线程对象调用start方法后, 只能等到对应的方法函数运行完毕.
# 也就是说一旦start后, 线程就属于失控状态. 对于函数中没有循环，可以使用join（）来结束循环。
# 方法一：一般的方法就是循环地判断一个标志位, 一旦标志位到达到预定的值, 就退出循环. 这样就能做到退出线程了.
# 直到我看到threading中Event对象。对于event.isSet()可以查看event的状态，set（）函数返回为True，clear（）函数返回为False。
# self.__flag.wait()
# 中self.__flag为True时立即返回, 为False时阻塞直到self.__flag为True后返回

import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到self.__flag为True后返回
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            time.sleep(1)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


def testFlag():
    print('step 1...')
    mythd = MyThread()
    mythd.start()

    time.sleep(3)
    print('step 2...')
    mythd.pause()

    time.sleep(10)
    print('step 3...')
    mythd.resume()

    time.sleep(2)
    print('step 4...')
    mythd.stop()

    print('step 5...')
    print('end...')


if __name__ == '__main__':
    testFlag()