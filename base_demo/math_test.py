import math
from math import *
from random import *


def testMath():
    print('abs', abs(-1))
    print('ceil', ceil(1.2))
    print('floor', floor(1.2))
    print('min', min(1, 2, 3, 4))
    print('max', max(1, 2, 3, 4))
    print('round', round(3.4))
    print('power', pow(2, 3))
    print('trunc', trunc(1.23))
    print('sin', sin(pi / 2))
    print('pi/2=>', degrees(pi / 2))
    print('180=>', radians(180))


def testRange():
    for i in range(10, 0, -2):
        print('id=%d' % i)
    i = 100
    sum = 0
    while i > 0:
        sum = sum + i
        i = i - 1
    print('sum=', sum)

def testRandom():
    for i in range(1, 5):
        print(random())
    # lst = []
    lst = list()
    print('type(range(1,11)', type(range(1, 11)))
    for i in range(1, 11):
        lst.append(i)
    print('lst=', lst)
    shuffle(lst)
    print('shuffle', lst)

    s = set()
    for i in range(1, 11):
        s.add(i)
    print('set', s)
    print('range', list(range(1, 10)))

    s = list()
    for i in range(1, 40):
        s.append(randrange(1, 10))
    print('randrange', s)
    s.sort(reverse=True)
    print('sort s', s)
    print(help(randrange))
    print(help(randint))


if __name__ == '__main__':
    testRange()
    testMath()
    testRandom()
    rlt = dir(math)
    print('type(rlt)=', type(rlt))
