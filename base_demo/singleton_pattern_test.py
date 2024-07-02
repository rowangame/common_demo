# https://www.cnblogs.com/huchong/p/8244279.html
# 单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类
# 只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场
import time
import threading

# 基于__new__方法实现（推荐使用，方便）
# 当我们实现单例时，为了保证线程安全需要在内部加入锁
#
# 我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），
# 实例化对象；然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    # see: java double-check locking for singleton mode
    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
                    # 每个类实例对象时,都会调用 __new__,__init__方法。
                    # 而这个单列模式只能在这里创建rlock锁。在__init__方法内创建rlock锁，
                    # 不是唯一的。不能保证数据安全
                    Singleton._instance.id = 0
                    Singleton._instance.lock = threading.RLock()
        return Singleton._instance

    # 通过使用
    # Lock
    # 对象可以非常方便地实现线程安全的类，线程安全的类具有如下特征：
    # 该类的对象可以被多个线程安全地访问。
    # 每个线程在调用该对象的任意方法之后，都将得到正确的结果。
    # 每个线程在调用该对象的任意方法之后，该对象都依然保持合理的状态。
    def increaseId(self):
        self.lock.acquire()
        try:
            # time.sleep(2)
            self.id = self.id + 1
            print("self.addr=%d self.id=%d self.id.addr=%d" % (id(self), self.id, id(self.id)))
        finally:
            self.lock.release()


def task(arg):
    print(type(arg), arg)
    obj = Singleton()
    obj.increaseId()
    # print("obj,id(obj.id),id(obj.lock)",obj,id(obj.id),id(obj.lock))


def testSingleton2():
    # obj1 = Singleton()
    # obj2 = Singleton()
    # obj1.increaseId()
    # obj2.increaseId()

    for i in range(2):
        t = threading.Thread(target=task, args=[i, ])
        t.start()


if __name__ == '__main__':
    # testSingleton1()
    testSingleton2()
