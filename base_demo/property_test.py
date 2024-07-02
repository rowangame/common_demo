# -*- coding: UTF-8 -*-
from retry import retry


class MyCls(object):
    def __init__(self):
        print('init...')
        super(MyCls, self).__init__()
        self._value = 0

    def __del__(self):
        print('delete...')

    def callback(self):
        print('callback ...')

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        del self._value

    @retry(tries=3, delay=1)
    def testSum(self):
        print('testSum...')
        return 1 / 0


if __name__ == '__main__':
    try:
        mycls = MyCls()
        print(mycls.value)

        mycls.value = 10
        print(mycls.value)
        if hasattr(mycls, 'value'):
            print('hasattr 1:', mycls.value)

        del mycls.value
        if hasattr(mycls, 'value'):
            print('hasattr 2:', mycls.value)

        mycls.testSum()
    except Exception as e:
        print('e1', e)
        print('e2', repr(e))
