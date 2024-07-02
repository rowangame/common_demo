import string
import sys


def testMemory():
    i = 1
    while i <= 10:
        print('id[%d]=%d' % (i, id(i)))
        i = i + 1


def testSize():
    a = [1, 2]
    b = [a, a]
    print('sizeof(a)=', sys.getsizeof(a))
    print('sizeof(b)=', sys.getsizeof(b))


def testId(input):
    print(('id=0x%x' % id(input)))


def testBase():
    s1 = sys.getsizeof("")
    s2 = sys.getsizeof([])
    s3 = sys.getsizeof(())
    s4 = sys.getsizeof(set())
    s5 = sys.getsizeof(dict())
    print(s1, s2, s3, s4, s5)


def testState():
    letters = "abcdefghijklmnopqrstuvwxyz"
    print("-------------------a----------------")
    a = []
    for i in letters:
        a.append(i)
        print('len(a)=%d size(a)=%d' % (len(a), sys.getsizeof(a)))

    print("-------------------b----------------")
    b = set()
    for j in letters:
        b.add(j)
        print('len(b)=%d size(b)=%d' % (len(b), sys.getsizeof(b)))

    print("-------------------c----------------")
    c = dict()
    for k in letters:
        c[k] = k
        print('len(c)=%d size(c)=%d' % (len(c), sys.getsizeof(c)))
    print(c)


if __name__ == '__main__':
    testMemory()
    testSize()
    testBase()
    num = 101
    print(('id=0x%x' % id(num)))
    testId(num)
    testState()
