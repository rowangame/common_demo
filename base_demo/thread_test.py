# Lock 和 RLock 的区别如下：
# threading.Lock：它是一个基本的锁对象，每次只能锁定一次，其余的锁请求，需等待锁释放后才能获取。
# threading.RLock：它代表可重入锁（Reentrant Lock）。对于可重入锁，
# 在同一个线程中可以对它进行多次锁定，也可以多次释放。如果使用 RLock，那么 acquire() 和 release() 方法必须成对出现。
# 如果调用了 n 次 acquire() 加锁，则必须调用 n 次 release() 才能释放锁。
import threading
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s:%s' % (threadName, time.ctime(time.time())))


def testThread1():
    try:
        t1 = threading.Thread(target=print_time, args=('thread-1', 2))
        t2 = threading.Thread(target=print_time, args=('thread-2', 4))
        print("step 1...")
        t1.start()
        print("step 2...")
        t2.start()
        print("step 3...")
        t1.join()
        print("step 4...")
        t2.join()
        print("step 5...")
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    testThread1()


