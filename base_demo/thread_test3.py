# 参考 https://blog.csdn.net/qq_33540705/article/details/90232209
# 1.信号量也提供acquire方法和release方法，每当调用acquire方法的时候，如果内部计数器大于0，则将其减1，
# 如果内部计数器等于0，则会阻塞该线程，知道有线程调用了release方法将内部计数器更新到大于1位置。
# class threading.Sempaphore(value = 1) --限制资源的并发访问。semaphore
# 是一个内部的计数器,它会随着acquire()的请求减小,也会随着release()的
# 释放增加。这个计数器的值不会小于零,当acquier() 发现计数器的值为0时,那么当前
# 对象会等待直到其他对象release()为止。acquier(blocking = True ,timeout = None)
# release()

import threading
import time


class MyTask(object):
    semp = threading.Semaphore(value=1)

    def __init__(self):
        super(MyTask, self).__init__()

    def doSomething(self, name, delay):
        try:
            MyTask.semp.acquire()
            print('running ...', id(self), name, delay)
            time.sleep(2)
        finally:
            MyTask.semp.release()


def testSemaphore():
    th1 = threading.Thread(target=MyTask().doSomething, args=('thread-1', 2))
    th2 = threading.Thread(target=MyTask().doSomething, args=('thread-2', 2))
    th1.start()
    th2.start()


if __name__ == '__main__':
    testSemaphore()
